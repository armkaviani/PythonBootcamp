import requests
from bs4 import BeautifulSoup

class ZillowScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }
        self.response = requests.get(self.url, headers=self.headers)
        self.data = self.response.text
        self.soup = BeautifulSoup(self.data, "html.parser")

    
    def get_links(self):
        all_link_ellemnts = self.soup.select(".StyledPropertyCardDataWrapper a")
        all_links = [link["href"] for link in all_link_ellemnts]
        print(f"There are {len(all_links)} links to individual listings in total: \n")
        print(all_links)

    
    def get_addresses(self):
        all_addresse_elements = self.soup.select(".StyledPropertyCardDataWrapper address")
        all_addresses = [address.get_text().replace("|", "").strip() for address in all_addresse_elements]
        print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")
        print(all_addresses)


    def get_prices(self):
        all_price_elements = self.soup.select(".PropertyCardWrapper span")
        all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
        print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")
        print(all_prices)

