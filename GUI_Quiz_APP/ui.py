from tkinter import *

THEME_COLOR = "#375362"

class QuizeInterface:

    def __init__(self):
        self.frame = Tk()
        self.frame.title("Quizzler")
        self.frame.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_board = Label(text="Score: 0", bg=THEME_COLOR, fg="White")
        self.score_board.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_img)
        self.false_button = Button(image=self.false_img)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)


        self.frame.mainloop()
