import smtplib
import datetime as dt


class BirthdayEmailer:
    def __init__(self, email, password, smtp_server="smtp.gmail.com"):
        self.email = email
        self.password = password
        self.smtp_server = smtp_server

    def get_today_tuple(self):
        today = dt.datetime.now()
        return today.day, today.month

