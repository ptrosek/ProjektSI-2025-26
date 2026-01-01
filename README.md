Kod wygenerowany za pomocą Jules(Gemini 3) oraz Gemini Code Assistant(Gemini 3 Pro)

## Wymagania

Python 3.12+ oraz https://docs.astral.sh/uv/getting-started/installation/

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

```uv run ./main.py --ticker EDMW.DE --start-date 2025-09-01 --pred-len 5 --lookback 63 --device cuda```
Wynik:
```
--- Backtest Results ---
Start                     2025-09-01 00:00:00
End                       2025-12-30 00:00:00
Duration                    120 days 00:00:00
Exposure Time [%]                    87.95181
Equity Final [$]                  10971.29418
Equity Peak [$]                   10971.29418
Return [%]                            9.71294
Buy & Hold Return [%]                 6.51539
Return (Ann.) [%]                    32.50391
Volatility (Ann.) [%]                11.69944
CAGR [%]                             21.49027
Sharpe Ratio                          2.77825
Sortino Ratio                         5.89831
Calmar Ratio                         11.96993
Alpha [%]                             5.88875
Beta                                  0.58695
Max. Drawdown [%]                    -2.71546
Avg. Drawdown [%]                    -0.82587
Max. Drawdown Duration       31 days 00:00:00
Avg. Drawdown Duration        8 days 00:00:00
# Trades                                   15
Win Rate [%]                         73.33333
Best Trade [%]                        2.21439
Worst Trade [%]                      -0.73194
Avg. Trade [%]                        0.65269
Max. Trade Duration          14 days 00:00:00
Avg. Trade Duration           6 days 00:00:00
Profit Factor                         7.90583
Expectancy [%]                        0.65644
SQN                                   2.80522
Kelly Criterion                       0.60515
_strategy                      SignalStrategy
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
Plot saved to EDMW.DE_backtest.html
```