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


    