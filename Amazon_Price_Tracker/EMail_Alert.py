import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

class EMailAlert:
    def __init__(self, title):
        self.email = os.environ["EMAIL_ADDRESS"]
        self.title = title
        self.smtp_mail = os.environ["SMTP_ADDRESS"]
        self.password = os.environ["EMAIL_PASSWORD"]
        

    def send_email(self, price_as_float, price_with_currency, url):
        PREIS = 35

        if price_as_float <= PREIS:
            message = f"{self.title} is on sale for {price_with_currency}!"
            with smtplib.SMTP(self.smtp_mail, 587) as connection:
                connection.starttls()
                connection.login(self.email, self.password)
                connection.sendmail(from_addr=self.email,
                                    to_addrs=self.email,
                                    msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8"))




    

        
