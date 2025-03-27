from tkinter import *
from tkinter import messagebox

class PasswordSaver:

    def __init__(self, website_field, email_field, password_field):
        self.website_field = website_field
        self.email_field = email_field
        self.password_field = password_field
    
    def save_password(self):
        website = self.website_field.get()
        email = self.email_field.get()
        password = self.password_field.get()

        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
            if is_ok:
                with open("data.txt", "a") as data_file:
                    data_file.write(f"{website} | {email} | {password}\n")
                self.website_field.delete(0, END)
                self.password_field.delete(0, END)

