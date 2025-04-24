import requests


class StockPrice:
    STOCK_NAME = "TSLA"
    STOCK_ENDPOINT = "https://www.alphavantage.co/query"
    STOCK_API_KEY = "BIRIG5133W1XXB2T"

    def __init__(self):
        self.stock_params = {"function": "TIME_SERIES_DAILY", "symbol": self.STOCK_NAME, "apikey": self.STOCK_API_KEY,}



