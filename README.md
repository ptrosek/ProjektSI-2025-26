Kod wygenerowany za pomocą Jules(Gemini 3) oraz Gemini Code Assistant(Gemini 3 Pro)

## Wymagania

Python 3.12+ oraz https://docs.astral.sh/uv/getting-started/installation/

## Model

https://huggingface.co/NeoQuasar/Kronos-base

End of knowledge dla tego modelu przypada na [02.2024](https://github.com/shiyu-coder/Kronos/issues/117#issuecomment-3341025476) roku, wszystkie backtesty obejmujące czas przed tą datą nie będą obiektywne.


## Konfiguracja

```
cd <nazwa_katalogu>
```

```
git clone https://github.com/shiyu-coder/Kronos.git
```

```
echo "" > Kronos/__init__.py
```

```
uv sync
```

## Przykładowe użycie 

```uv run ./main.py --ticker SPY --start-date 2025-09-01 --pred-len 1 --lookback 63 --device cuda```
Wynik:
```
--- Backtest Results ---
Start                     2025-09-02 00:00:00
End                       2025-12-31 00:00:00
Duration                    120 days 00:00:00
Exposure Time [%]                    65.88235
Equity Final [$]                  10685.91677
Equity Peak [$]                    10735.0569
Return [%]                            6.85917
Buy & Hold Return [%]                 7.11593
Return (Ann.) [%]                    21.73584
Volatility (Ann.) [%]                 9.20926
CAGR [%]                             14.94888
Sharpe Ratio                          2.36022
Sortino Ratio                          4.0246
Calmar Ratio                          6.80459
Alpha [%]                              4.2728
Beta                                  0.36346
Max. Drawdown [%]                    -3.19429
Avg. Drawdown [%]                    -0.79731
Max. Drawdown Duration       13 days 00:00:00
Avg. Drawdown Duration        9 days 00:00:00
# Trades                                   22
Win Rate [%]                         63.63636
Best Trade [%]                        1.46842
Worst Trade [%]                      -0.75243
Avg. Trade [%]                         0.3343
Max. Trade Duration          11 days 00:00:00
Avg. Trade Duration           3 days 00:00:00
Profit Factor                         3.05282
Expectancy [%]                        0.33654
SQN                                   2.27841
Kelly Criterion                       0.42532
_strategy                      SignalStrategy
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
Plot saved to SPY_backtest.html
Generating comparison plot...

--- Model Performance Metrics ---
Correlation: 0.1266
RMSE: 0.0090
MAE: 0.0071
Directional Accuracy: 46.43%
Combined analysis and backtest saved to SPY_backtest.html
```