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

    
    def submit_form_entries(self):
        for i in range(len(self.all_links)):
            self.driver.get(self.form_url)
            time.sleep(2)

            try:
                address_input = self.driver.find_element(By.XPATH,
                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
                price_input = self.driver.find_element(By.XPATH,
                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
                link_input = self.driver.find_element(By.XPATH,
                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
                submit_button = self.driver.find_element(By.XPATH,
                    '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

                address_input.send_keys(self.all_addresses[i])
                price_input.send_keys(self.all_prices[i])
                link_input.send_keys(self.all_links[i])
                submit_button.click()
            except Exception as e:
                print(f"Error submitting entry {i + 1}: {e}")
