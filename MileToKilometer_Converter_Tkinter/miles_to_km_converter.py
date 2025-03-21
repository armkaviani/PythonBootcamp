from tkinter import *
from converter_logic import ConverterLogic


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
   
        # Label: "is equal to"
        self.is_equal_label = Label(text="is equal to")
        self.is_equal_label.grid(column=0, row=1)

        # Label: Result (Initially "0")
        self.kilometer_result_label = Label(text="0")
        self.kilometer_result_label.grid(column=1, row=1)

        # Label: "Km"
        self.kilometer_label = Label(text="Km")
        self.kilometer_label.grid(column=2, row=1)

        # Button: "Calculate"
        self.calculate_button = Button(text="Calculate")
        self.calculate_button.grid(column=1, row=2)

   
    def convert(self):
        miles = float(self.miles_input.get())  # Get input from entry field
        km = ConverterLogic.miles_to_km(miles)  # Call the conversion function
        self.kilometer_result_label.config(text=f"{km}")  # Update label
        
     
    def run(self):
        self.window.mainloop()