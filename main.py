"""Run weekly technical indicator analysis for selected stocks."""

from __future__ import annotations

from data.fetcher import fetch_weekly_history
from indicators.technical import add_core_indicators
from strategy.weekly_report import format_weekly_summary


SYMBOLS = ["AAPL", "MSFT", "NVDA"]


def analyze_symbol(symbol: str) -> str:
    """Fetch, calculate indicators, and return a summary for a stock."""
    history = fetch_weekly_history(symbol)
    enriched = add_core_indicators(history)
    return format_weekly_summary(symbol, enriched)


def main() -> None:
    print("Weekly Technical Indicator Analysis")
    print("=" * 40)

    for symbol in SYMBOLS:
        try:
            report = analyze_symbol(symbol)
            print(report)
        except Exception as exc:  # noqa: BLE001
            print(f"\n{symbol}: failed to analyze ({exc})")


if __name__ == "__main__":
    main()
