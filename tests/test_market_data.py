from app.market_data import MarketDataFetcher

def test_fetch_data():
    fetcher = MarketDataFetcher()
    data = fetcher.fetch_data()
    assert isinstance(data, dict)
    for symbol, df in data.items():
        assert hasattr(df, "columns")