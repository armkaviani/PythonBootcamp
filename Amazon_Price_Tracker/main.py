from ScrapePrice import ScrapePrice
from EMail_Alert import EMailAlert

def main():

    scrape_price = ScrapePrice()
    price_as_float, price_with_currency, title = scrape_price.get_price()

    email_alert = EMailAlert(title)
    email_alert.send_email(price_as_float, price_with_currency, scrape_price.url)


if __name__ == "__main__":
    main()
