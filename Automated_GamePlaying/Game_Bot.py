from selenium import webdriver
from selenium.webdriver.common.by import By

class CookieClickerBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://orteil.dashnet.org/experiments/cookie/")
