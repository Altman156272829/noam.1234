# Weekly Stock Technical Indicator Analyzer

This project fetches weekly market data and analyzes technical indicators for:
- AAPL
- MSFT
- NVDA

## Indicators included
- RSI (14)
- MACD (12, 26, 9)
- 50-week moving average
- 200-week moving average

## Project structure
- `data/` : market data fetching with `yfinance`
- `indicators/` : RSI, MACD, and moving average calculations
- `strategy/` : simple signal generation and reporting
- `main.py` : entry point that runs the analysis

## Run
```bash
pip install -r requirements.txt
python main.py
```
