import click
import yfinance as yf
import pandas as pd
import os
from backtesting import Backtest
from predictor import KronosWrapper
from strategy import SignalStrategy
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

@click.command()
@click.option('--ticker', required=True, help='Ticker symbol (e.g., AAPL, BTC-USD)')
@click.option('--start-date', default='2025-09-01', help='Backtest start date (YYYY-MM-DD)')
@click.option('--rebalance', type=click.Choice(['daily', 'weekly', 'monthly']), default='daily', help='Rebalancing frequency')
@click.option('--initial-cash', default=10000, help='Initial capital')
@click.option('--device', default='cpu', help='Device to run model on (cpu or cuda)')
@click.option('--pred-len', default=21, help='Prediction length in days')
@click.option('--lookback', default=126, help='Lookback period for model input in days')
def run_backtest(ticker, start_date, rebalance, initial_cash, device, pred_len, lookback):
    """
    Runs a backtest for the selected ticker using Kronos-base signals.
    """
    click.echo(f"Starting backtest for {ticker} from {start_date} with {rebalance} rebalancing...")

    # 1. Fetch Data
    click.echo("Fetching data...")
    # We fetch a bit more history for the lookback context
    # Lookback is 50 in predictor default.
    lookback_buffer_days = 100 
    start_dt = pd.to_datetime(start_date)
    fetch_start = start_dt - pd.Timedelta(days=lookback_buffer_days)
    
    # yfinance expects string date
    data = yf.download(ticker, start=fetch_start.strftime('%Y-%m-%d'), progress=False)
    
    if data.empty:
        click.echo("Error: No data found for ticker.")
        return

    # Flatten MultiIndex columns if present (common in new yfinance)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
        
    # Ensure columns lower case
    data.columns = [c.lower() for c in data.columns]
    
    # 2. Generate Signals
    click.echo("Initializing Kronos model...")
    predictor = KronosWrapper(device=device)
    
    click.echo("Generating signals (this may take a while)...")
    # Predictor generates signals for the whole dataframe, but valid only after lookback
    generated_data = predictor.generate_signals(data, start_date=start_date, lookback=lookback, pred_len=pred_len)
    
    # Add signals and predicted returns to dataframe
    data['Signal'] = generated_data['Signal']
    data['Pred_Return'] = generated_data['Pred_Return']
    
    # Calculate Actual Return for comparison
    data['Actual_Return'] = data['close'].pct_change(pred_len).shift(-pred_len)
    
    # 3. Prepare for Backtest
    # Filter data to start from start_date for the actual backtest run
    backtest_data = data[data.index >= start_dt].copy()
    
    # Ensure correct columns for backtesting.py (Title Case: Open, High, Low, Close, Volume)
    rename_map = {
        'open': 'Open',
        'high': 'High',
        'low': 'Low',
        'close': 'Close',
        'volume': 'Volume'
    }
    backtest_data = backtest_data.rename(columns=rename_map)
    
    # Configure Strategy
    SignalStrategy.rebalance_freq = rebalance
    
    # 4. Run Backtest
    click.echo("Running backtest...")
    bt = Backtest(backtest_data, SignalStrategy, cash=initial_cash, commission=0, finalize_trades=True)
    stats = bt.run()
    
    click.echo("\n--- Backtest Results ---")
    click.echo(stats)
    
    # 5. Plot
    output_file = f"{ticker}_backtest.html"
    bt.plot(filename=output_file, open_browser=False)
    click.echo(f"Plot saved to {output_file}")

    # 6. Compare Predicted vs Actual Returns
    click.echo("Generating comparison plot...")
    
    # Filter for valid actual returns (drop last pred_len rows which are NaN)
    valid_comparison = backtest_data.dropna(subset=['Actual_Return', 'Pred_Return'])
    
    if not valid_comparison.empty:
        # Calculate Statistical Metrics
        if len(valid_comparison) < 2 or valid_comparison['Actual_Return'].std() == 0 or valid_comparison['Pred_Return'].std() == 0:
            correlation = 0.0
        else:
            correlation = valid_comparison['Actual_Return'].corr(valid_comparison['Pred_Return'])

        rmse = np.sqrt(((valid_comparison['Actual_Return'] - valid_comparison['Pred_Return']) ** 2).mean())
        mae = (valid_comparison['Actual_Return'] - valid_comparison['Pred_Return']).abs().mean()
        
        # Directional Accuracy
        actual_dir = np.sign(valid_comparison['Actual_Return'])
        pred_dir = np.sign(valid_comparison['Pred_Return'])
        directional_acc = (actual_dir == pred_dir).mean()

        click.echo("\n--- Model Performance Metrics ---")
        click.echo(f"Correlation: {correlation:.4f}")
        click.echo(f"RMSE: {rmse:.4f}")
        click.echo(f"MAE: {mae:.4f}")
        click.echo(f"Directional Accuracy: {directional_acc:.2%}")

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 18))
        
        # 1. Time Series Plot
        ax1.plot(valid_comparison.index, valid_comparison['Actual_Return'], label='Actual Return', color='black', alpha=0.6, linewidth=1)
        ax1.plot(valid_comparison.index, valid_comparison['Pred_Return'], label='Predicted Return', color='blue', alpha=0.8, linewidth=1.5)
        ax1.set_title(f'Time Series: Actual vs Predicted {pred_len}-Day Returns')
        ax1.set_ylabel('Return')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # 2. Scatter Plot with y=x line
        ax2.scatter(valid_comparison['Actual_Return'], valid_comparison['Pred_Return'], alpha=0.5, c='blue', edgecolors='none', label='Predictions')
        
        # Determine limits for y=x line
        all_vals = np.concatenate([valid_comparison['Actual_Return'], valid_comparison['Pred_Return']])
        min_val, max_val = np.min(all_vals), np.max(all_vals)
        ax2.plot([min_val, max_val], [min_val, max_val], 'r--', label='Perfect Prediction (y=x)')
        
        ax2.set_xlabel(f'Actual {pred_len}-Day Return')
        ax2.set_ylabel(f'Predicted {pred_len}-Day Return')
        ax2.set_title(f'Scatter: Correlation Analysis (Corr: {correlation:.2f}, Dir Acc: {directional_acc:.1%})')
        ax2.axhline(0, color='gray', linestyle='-', alpha=0.3)
        ax2.axvline(0, color='gray', linestyle='-', alpha=0.3)
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # 3. Prediction Error Plot (Residuals)
        # Calculate residuals: Actual - Predicted
        residuals = valid_comparison['Actual_Return'] - valid_comparison['Pred_Return']
        ax3.scatter(valid_comparison.index, residuals, alpha=0.5, c='purple', edgecolors='none', label='Prediction Error')
        ax3.axhline(0, color='gray', linestyle='--', alpha=0.5)
        ax3.set_title('Prediction Error (Actual - Predicted) over Time')
        ax3.set_ylabel('Error')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save plot to buffer for HTML embedding
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png', bbox_inches='tight')
        img_buf.seek(0)
        img_data = base64.b64encode(img_buf.read()).decode('utf-8')
        img_buf.close()

        # Append analysis to Backtest HTML
        # Generate Investment Suggestion
        last_row = backtest_data.iloc[-1]
        cur_pred = last_row['Pred_Return']
        cur_date = last_row.name.strftime('%Y-%m-%d')
        rec_color = "green" if cur_pred > 0 else "red"
        rec_action = "BUY" if cur_pred > 0 else "SELL"

        suggestion_html = f"""
        <div style="font-family: sans-serif; margin: 20px; padding: 20px; border: 1px solid #ccc; background: #f9f9f9; border-left: 6px solid {rec_color};">
            <h2>Investment Suggestion ({cur_date})</h2>
            <p><strong>Recommendation:</strong> <span style="color: {rec_color}; font-weight: bold;">{rec_action}</span> (Predicted Return: {cur_pred:.2%})</p>
        </div>
        """

        stats_html = f"""
        <div style="font-family: sans-serif; margin: 20px; padding: 20px; border: 1px solid #ccc; background: #f9f9f9;">
            <h2>Backtest Statistics</h2>
            {stats.to_frame(name='Value').to_html(classes="table", border=0)}
        </div>
        """

        metrics_html = f"""
        <div style="font-family: sans-serif; margin: 20px; padding: 20px; border: 1px solid #ccc; background: #f9f9f9;">
            <h2>Model Performance Metrics</h2>
            <p><strong>Correlation:</strong> {correlation:.4f}</p>
            <p><strong>RMSE(Root Mean Square Error):</strong> {rmse:.4f}</p>
            <p><strong>MAE(Mean Absolute Error):</strong> {mae:.4f}</p>
            <p><strong>Directional Accuracy:</strong> {directional_acc:.2%}</p>
        </div>
        """
        plot_html = f'<div style="margin: 20px; text-align: center;"><img src="data:image/png;base64,{img_data}" style="max-width: 100%; border: 1px solid #ddd;"></div>'
        data_html = f'<div style="margin: 20px; overflow-x: auto;"><h3>Comparison Data</h3>{valid_comparison.to_html(classes="table", border=0)}</div>'
        
        with open(output_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        # Inject content before closing body tag
        if '</body>' in html_content:
            # Inject suggestion at the top (after <body>)
            if '<body>' in html_content:
                html_content = html_content.replace('<body>', f'<body>{suggestion_html}')
            final_html = html_content.replace('</body>', f'{stats_html}{metrics_html}{plot_html}{data_html}</body>')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(final_html)
            click.echo(f"Combined analysis and backtest saved to {output_file}")
        else:
            # Fallback if </body> not found
            with open(output_file, 'a', encoding='utf-8') as f:
                f.write(stats_html + metrics_html + plot_html + data_html)
            click.echo(f"Appended analysis to {output_file}")
    else:
        click.echo("Not enough data to generate comparison (need at least 21 days past start date).")

if __name__ == '__main__':
    run_backtest()
