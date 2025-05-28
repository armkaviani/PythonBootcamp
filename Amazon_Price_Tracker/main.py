from ScrapePrice import ScrapePrice


def main():

    scrape_price = ScrapePrice()
    price_as_float, price_with_currency, title = scrape_price.get_price()


if __name__ == "__main__":
    main()
