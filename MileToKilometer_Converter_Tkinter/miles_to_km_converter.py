from tkinter import *


class MilesToKmConverter:
        
    def __init__(self):
        self.window = Tk()
        self.window.title("Miles to Kilometer Converter")
        self.window.config(padx=20, pady=20)

        self.create_widgets()

    def create_widgets(self):
        #Entry for miles
        self.miles_input = Entry(width=7)
        self.miles_input.grid(column=1, row=0)

        # Label for "Miles"
        self.miles_label = Label(text="Miles")
        self.miles_label.grid(column=2, row=0)
   