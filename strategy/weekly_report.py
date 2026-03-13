"""Simple strategy interpretation layer for weekly indicators."""

from __future__ import annotations

import pandas as pd


def generate_signal(latest_row: pd.Series) -> str:
    """Generate a lightweight directional signal from indicators."""
    bullish_trend = latest_row["SMA_50"] > latest_row["SMA_200"]
    bullish_momentum = latest_row["MACD"] > latest_row["MACD_SIGNAL"]
    neutral_rsi = 40 <= latest_row["RSI_14"] <= 70

    if bullish_trend and bullish_momentum and neutral_rsi:
        return "Bullish bias"
    if (not bullish_trend) and (not bullish_momentum):
        return "Bearish bias"
    return "Mixed / watchlist"


def format_weekly_summary(symbol: str, data: pd.DataFrame) -> str:
    """Create a readable one-block report for the latest week."""
    latest = data.iloc[-1]

    return (
        f"\n{symbol} Weekly Snapshot\n"
        f"{'-' * 32}\n"
        f"Close: {latest['Close']:.2f}\n"
        f"RSI(14): {latest['RSI_14']:.2f}\n"
        f"MACD: {latest['MACD']:.4f}\n"
        f"MACD Signal: {latest['MACD_SIGNAL']:.4f}\n"
        f"SMA 50: {latest['SMA_50']:.2f}\n"
        f"SMA 200: {latest['SMA_200']:.2f}\n"
        f"Signal: {generate_signal(latest)}"
    )
