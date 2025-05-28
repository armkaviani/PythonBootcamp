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



    

        
