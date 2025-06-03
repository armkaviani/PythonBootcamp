from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os
from dotenv import load_dotenv

load_dotenv()

class AutoLoginManager:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get( "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
                        "&keywords=python%20developer"
                        "&location=London%2C%20England%2C%20United%20Kingdom"
                        "&redirect=false&position=1&pageNum=0")
        self.username = os.environ["E_MAIL"]
        self.password = os.environ["PASSWORD"]
        self.phone = os.environ["PHONE"]


    def login_manager(self):
        time.sleep(2)
        sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
        sign_in_button.click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_key"]').send_keys(self.username)
        self.driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_password"]').send_keys(self.password)
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button'))
        ).click()


    def auto_apply(self):
        apply_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)
        phone = self.driver.find_element(By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.get_attribute("value") == "":
            phone.send_keys(self.phone)
        submit_button = self.driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        submit_button.click()