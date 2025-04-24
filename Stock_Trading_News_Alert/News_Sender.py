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



