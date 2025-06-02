from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CookieClickerBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://orteil.dashnet.org/experiments/cookie/")

        self.cookie = self.driver.find_element(By.ID, "cookie")
        items = self.driver.find_elements(By.CSS_SELECTOR, "#store div")
        self.item_ids = [item.get_attribute("id") for item in items]

        self.timeout = time.time() + 5
        self.five_min = time.time() + 60*5

    def click_cookie(self):
        self.cookie.click()

    
    def get_item_prices(self):
        all_prices = self.driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []
        for price in all_prices:
            text = price.text
            if text != "":
                cost = int(text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        return item_prices