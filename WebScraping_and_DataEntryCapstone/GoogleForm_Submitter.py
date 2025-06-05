from selenium import webdriver
from selenium.webdriver.common.by import By


class GoogleFormSubmitter:
    def __init__(self, form_url, addresses, prices, links):
        self.form_url = form_url
        self.all_addresses = addresses
        self.all_prices = prices
        self.all_links = links
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        
