from Zillow_Scraper import ZillowScraper

def main():
    scraper = ZillowScraper("https://appbrewery.github.io/Zillow-Clone/")
    scraper.get_links()
    scraper.get_addresses()
    scraper.get_prices()

if __name__ == "__main__":
    main()