import yfinance as yf
import pandas as pd
from app.config import Config

class MarketDataFetcher:
    def __init__(self, symbols: list[str] = None, interval: str = None):
        self.symbols = symbols or Config.STOCK_SYMBOLS
        self.interval = interval or Config.DATA_INTERVAL

    def fetch_data(self) -> dict:
        """
        Fetches historical market data for each symbol.
        Returns a dictionary mapping symbol to its pandas DataFrame.
        """
        data = {}
        for symbol in self.symbols:
            try:
                ticker = yf.Ticker(symbol)
                hist = ticker.history(period="1mo", interval=self.interval)
                data[symbol] = hist if not hist.empty else pd.DataFrame()
            except Exception as e:
                data[symbol] = pd.DataFrame()
        return data