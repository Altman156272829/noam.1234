"""Technical indicator calculations."""

from __future__ import annotations

import pandas as pd


def compute_rsi(close: pd.Series, period: int = 14) -> pd.Series:
    """Compute Relative Strength Index (RSI)."""
    delta = close.diff()
    gains = delta.clip(lower=0)
    losses = -delta.clip(upper=0)

    avg_gain = gains.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    avg_loss = losses.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def compute_macd(
    close: pd.Series,
    fast_period: int = 12,
    slow_period: int = 26,
    signal_period: int = 9,
) -> tuple[pd.Series, pd.Series, pd.Series]:
    """Compute MACD line, signal line, and histogram."""
    ema_fast = close.ewm(span=fast_period, adjust=False).mean()
    ema_slow = close.ewm(span=slow_period, adjust=False).mean()

    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
    histogram = macd_line - signal_line

    return macd_line, signal_line, histogram


def add_moving_averages(data: pd.DataFrame, short_window: int = 50, long_window: int = 200) -> pd.DataFrame:
    """Append 50 and 200 period simple moving averages to the dataset."""
    enriched = data.copy()
    enriched[f"SMA_{short_window}"] = enriched["Close"].rolling(window=short_window, min_periods=1).mean()
    enriched[f"SMA_{long_window}"] = enriched["Close"].rolling(window=long_window, min_periods=1).mean()
    return enriched


def add_core_indicators(data: pd.DataFrame) -> pd.DataFrame:
    """Add RSI, MACD, signal, histogram, and moving averages columns."""
    enriched = add_moving_averages(data, short_window=50, long_window=200)
    enriched["RSI_14"] = compute_rsi(enriched["Close"], period=14)

    macd_line, signal_line, histogram = compute_macd(enriched["Close"])
    enriched["MACD"] = macd_line
    enriched["MACD_SIGNAL"] = signal_line
    enriched["MACD_HIST"] = histogram

    return enriched
