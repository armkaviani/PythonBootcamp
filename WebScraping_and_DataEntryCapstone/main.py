from Zillow_Scraper import ZillowScraper
from GoogleForm_Submitter import GoogleFormSubmitter

def main():
    scraper = ZillowScraper("https://appbrewery.github.io/Zillow-Clone/")
    scraper.get_links()
    scraper.get_addresses()
    scraper.get_prices()

    submitter = GoogleFormSubmitter("https://docs.google.com/forms/d/e/1FAIpQLSfR5jYLE0TQqSj7d0xpsrGDStC9VwG3aZv7EkVhQRnDj_v2PQ/viewform?usp=header",
                                    scraper.all_addresses,
                                    scraper.all_prices,
                                    scraper.all_links)
    submitter.submit_form_entries()
    

if __name__ == "__main__":
    main()