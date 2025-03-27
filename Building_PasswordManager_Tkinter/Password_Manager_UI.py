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
