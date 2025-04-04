from tkinter import *

class KanyeUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Kanye says ...")
        self.window.config(padx=50, pady=50)

        self.canvas = Canvas(width=300, height=414)
        self.photo_background = PhotoImage(file="background.png")
        self.canvas.create_image(150, 207, image=self.photo_background)
        self.quote_text = self.canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
        self.canvas.grid(row=0, column=0)

        self.kanye_button_image = PhotoImage(file="kanye.png")
        self.kanye_button = Button(image=self.kanye_button_image, highlightthickness=0)
        self.kanye_button.grid(row=1, column=0)
        


    def run(self):
        self.window.mainloop()
