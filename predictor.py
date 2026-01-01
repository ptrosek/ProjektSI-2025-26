import sys
import os
import torch
import pandas as pd

# Add Kronos to path to import its modules
sys.path.append(os.path.join(os.path.dirname(__file__), "Kronos"))

try:
    from Kronos.model import Kronos, KronosTokenizer, KronosPredictor
except ImportError as e:
    # Fail gracefully if Kronos is not in the path correctly or structure differs
    print(f"Error: Could not import Kronos modules. Ensure the 'Kronos' repository is cloned in the same directory. Details: {e}")
    sys.exit(1)

class KronosWrapper:
    def __init__(self, device: str = "cuda" if torch.cuda.is_available() else "cpu", max_context: int = 512):
        self.device = device
        self.max_context = max_context
        self.tokenizer = None
        self.model = None
        self.predictor = None
        self._load_model()

    def _load_model(self):
        """Loads the pre-trained Kronos model and tokenizer."""
        print(f"Loading Kronos model on {self.device}...")
        try:
            self.tokenizer = KronosTokenizer.from_pretrained("NeoQuasar/Kronos-Tokenizer-base")
            self.model = Kronos.from_pretrained("NeoQuasar/Kronos-base")
            self.model.to(self.device)
            self.predictor = KronosPredictor(self.model, self.tokenizer, device=self.device, max_context=self.max_context)
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
            raise

    def predict_next_movement(self, df: pd.DataFrame, lookback: int = 50, pred_len: int = 21) -> float:
        """
        Predicts the percentage change of the close price for the next 'pred_len' steps.
        """
        # Ensure minimal columns
        required_cols = ['open', 'high', 'low', 'close']
        if not all(col in df.columns for col in required_cols):
            raise ValueError(f"DataFrame must contain {required_cols}")

        # Prepare input data
        if len(df) < lookback:
            return 0.0

        sub_df = df.iloc[-lookback:].copy()
        
        if 'timestamps' not in sub_df.columns:
            sub_df['timestamps'] = sub_df.index
            
        x_timestamp = sub_df['timestamps']
        
        # FIX: Generate y_timestamp for ALL prediction steps
        last_ts = x_timestamp.iloc[-1]
        # Assuming daily data. For 21 days, we generate 21 future dates.
        y_timestamp = pd.Series([last_ts + pd.Timedelta(days=i+1) for i in range(pred_len)])

        # Run prediction
        try:
            pred_df = self.predictor.predict(
                df=sub_df,
                x_timestamp=x_timestamp,
                y_timestamp=y_timestamp,
                pred_len=pred_len,  # Pass the correct length
                T=1.0,
                top_p=0.9,
                sample_count=1
            )
            
            # Calculate return: (Predicted_Close_at_t+21 - Last_Known_Close) / Last_Known_Close
            last_close = sub_df['close'].iloc[-1]
            final_pred_close = pred_df['close'].iloc[-1] # Take the last predicted value
            print(f"Predicted close after {pred_len} steps: {final_pred_close}, Last known close: {last_close}")
            return (final_pred_close - last_close) / last_close
            
        except Exception as e:
            print(f"Prediction error: {e}")
            return 0.0

    def generate_signals(self, df: pd.DataFrame, start_date: str, lookback: int = 50, threshold: float = 0.00, pred_len: int = 21) -> pd.DataFrame:
        """
        Generates buy/sell signals for the backtest period.
        
        Args:
            df: Full historical dataframe.
            start_date: Start date for signal generation.
            lookback: Context window size.
            threshold: Return threshold for a signal.
            pred_len: Prediction length in days.
            
        Returns:
            pd.DataFrame with columns 'Signal' and 'Pred_Return' indexed by date.
            Signal at index 't' represents the trade decision for 't+1' open.
            (e.g., if Close_t+1 > Close_t, Signal_t = 1)
        """
        print(f"Generating signals starting from {start_date}...")
        
        if isinstance(start_date, str):
            start_ts = pd.Timestamp(start_date)
        else:
            start_ts = start_date
            
        # Ensure df index is datetime
        if not isinstance(df.index, pd.DatetimeIndex):
            df.index = pd.to_datetime(df.index)
            
        signals = pd.Series(0, index=df.index)
        pred_returns = pd.Series(0.0, index=df.index)
        
        try:
            # find the first index >= start_ts
            start_idx = df.index.get_indexer([start_ts], method='bfill')[0]
        except:
            print("Start date outside of data range.")
            return signals

        total_steps = len(df) - start_idx
        
        # We iterate through the days.
        # For each day 'i' (starting from start_idx), we use data up to 'i' to predict 'i+1'.
        # The signal generated at 'i' will be executed by backtesting.py at the OPEN of 'i+1'.
        
        for i in range(start_idx, len(df)):
            # We need at least 'lookback' data points ending at 'i'
            if i < lookback:
                continue
                
            current_date = df.index[i]
            
            # Data available is inclusive of 'i'. 
            # slice in pandas iloc[start:end] is exclusive of end. So [i-lookback+1 : i+1] gives us 'lookback' rows ending at i.
            history_df = df.iloc[i-lookback+1 : i+1].copy()
            
            pred_return = self.predict_next_movement(history_df, lookback=lookback, pred_len=pred_len)
            pred_returns.iloc[i] = pred_return
            
            # Generate signal for 'i' (to trade tomorrow)
            if pred_return > threshold:
                signals.iloc[i] = 1
            else:
                signals.iloc[i] = 0
            print(f"Date: {current_date.date()} Predicted Return: {pred_return:.4f} Signal: {signals.iloc[i]}")
                
            if (i - start_idx) % 10 == 0:
                print(f"Processed {i - start_idx}/{total_steps} steps. Date: {current_date.date()} Pred Return: {pred_return:.4f}")
                
        return pd.DataFrame({'Signal': signals, 'Pred_Return': pred_returns})
