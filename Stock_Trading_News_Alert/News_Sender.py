import requests
from twilio.rest import Client


class GetNews:
    NEWS_API_KEY = "e34f452b25d746db9ca9709a32c18ccc"
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    COMPANY_NAME = "Tesla Inc"


    def __init__(self, twilio_sid, twilio_auth, from_number, to_number):
            self.client = Client(twilio_sid, twilio_auth)
            self.from_number = from_number
            self.to_number = to_number


    def fetch_articles(self):
            params = {"apikey": self.NEWS_API_KEY, "qInTitle": self.COMPANY_NAME}
            articles = requests.get(self.NEWS_ENDPOINT, params=params).json()["articles"]
            return articles[:3]


    def send_articles(self, stock_symbol, up_down, diff_percent):
        articles = self.fetch_articles()
        messages = [
            f"{stock_symbol}: {up_down}{diff_percent}%\nHeadline: {a['title']}\nBrief: {a['description']}"
            for a in articles
        ]

        for msg in messages:
            self.client.messages.create(body=msg, from_=self.from_number, to=self.to_number)


