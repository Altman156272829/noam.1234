"""Data fetching utilities for stock analysis."""

from __future__ import annotations

import yfinance as yf
import pandas as pd


REQUIRED_COLUMNS = ["Open", "High", "Low", "Close", "Volume"]


def fetch_weekly_history(symbol: str, period: str = "5y") -> pd.DataFrame:
    """Fetch weekly OHLCV history for a ticker symbol."""
    history = yf.download(symbol, period=period, interval="1wk", auto_adjust=False, progress=False)

    if history.empty:
        raise ValueError(f"No data returned for symbol '{symbol}'.")

    history = history.dropna(subset=["Close"]).copy()

    for column in REQUIRED_COLUMNS:
        if column not in history.columns:
            raise ValueError(f"Expected column '{column}' missing from downloaded data for '{symbol}'.")

    return history
