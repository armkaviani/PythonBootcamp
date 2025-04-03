from Birthday_Email import BirthdayEmailer

def main():
    my_email = "your_mail@gmail.com"
    my_pass = "your_pass"
    emailer = BirthdayEmailer(my_email, my_pass)
    emailer.send_birthday_email()

if __name__ == "__main__":
    main()