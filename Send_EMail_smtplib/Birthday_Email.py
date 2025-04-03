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

    def load_birthdays(self, file_path="birthdays.csv"):
        lines = pd.read_csv(file_path)
        return {(row['day'], row['month']): row for (index, row) in lines.iterrows()}
    
    def load_letter_template(self, file_path="letter.txt"):
        with open(file_path) as text:
            return text.read()
        
    def send_email(self, recipient_email, subject, body):
        with smtplib.SMTP(self.smtp_server) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(from_addr=self.email,
                                to_addrs=recipient_email,
                                msg=f"Subject:{subject}\n\n{body}")
