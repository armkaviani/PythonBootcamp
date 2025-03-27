from tkinter import *

class PasswordManagerUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50)
    
        self.canvas = Canvas(height=200, width=200)
        self.logo_img = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(row=0, column=1)

        # Labels
        Label(text="Website:").grid(row=1, column=0)
        Label(text="Email/Username:").grid(row=2, column=0)
        Label(text="Password:").grid(row=3, column=0)

        # Entries
        self.website_entry = Entry(width=35)
        self.website_entry.grid(row=1, column=1, columnspan=2)
        self.website_entry.focus()
        self.email_entry = Entry(width=35)
        self.email_entry.grid(row=2, column=1, columnspan=2)
        self.email_entry.insert(0, "example@gmail.com")
        self.password_entry = Entry(width=21)
        self.password_entry.grid(row=3, column=1)

        # Buttons
        self.generate_password_button = Button(text="Generate Password")
        self.generate_password_button.grid(row=3, column=2)

        self.add_button = Button(text="Add", width=36)
        self.add_button.grid(row=4, column=1, columnspan=2)

    def run(self):
        self.window.mainloop()



