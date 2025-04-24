import requests


class GetNews:
    NEWS_API_KEY = "e34f452b25d746db9ca9709a32c18ccc"
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    COMPANY_NAME = "Tesla Inc"

def fetch_articles(self):
        params = {"apikey": self.NEWS_API_KEY, "qInTitle": self.COMPANY_NAME}
        articles = requests.get(self.NEWS_ENDPOINT, params=params).json()["articles"]
        return articles[:3]
