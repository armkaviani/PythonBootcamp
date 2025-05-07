import requests


class StockPrice:
    STOCK_NAME = "TSLA"
    STOCK_ENDPOINT = "https://www.alphavantage.co/query"
    STOCK_API_KEY = "BIRIG5133W1XXB2T"

    def __init__(self):
        self.stock_params = {"function": "TIME_SERIES_DAILY", "symbol": self.STOCK_NAME, "apikey": self.STOCK_API_KEY,}


    def check_price_difference(self):    
        data = requests.get(self.STOCK_ENDPOINT, params=self.params).json()["Time Series (Daily)"] 
        data_list = [value for (key, value) in data.items()]
        yesterday = float(data_list[0]['4. close'])
        before_yesterday = float(data_list[1]['4. close'])


        diff = abs(yesterday - before_yesterday)
        percent = round((diff / yesterday) * 100)
        up_down = "🔺" if (yesterday > before_yesterday) else "🔻"

        return percent > 5, percent, up_down

