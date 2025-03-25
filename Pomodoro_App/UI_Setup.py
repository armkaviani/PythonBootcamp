from tkinter import *
from Timer_Mechanism import TimerMechanism
from Reset_Mechanism import ResetMechanism

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

class UISetup:
    def __init__(self):
        self.root = Tk()
        self.root.title("Pomodoro")
        self.root.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)

        self.timer_mechanism = TimerMechanism(self)
        self.reset_mechanism = ResetMechanism(self.timer_mechanism)

        self.canvas = Canvas(self.root, width=200, height=224, bg=YELLOW)
        self.tomato_img = PhotoImage(file="tomato.png")
        self.canvas.create_image(102, 112, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(column=1, row=1)

        self.title_label = Label(self.root, text="Timer", bg=YELLOW, font=(FONT_NAME, 50, "bold"), fg=GREEN)
        self.title_label.grid(column=1, row=0) 

        self.start_button = Button(self.root, text="Start", highlightthickness=0, command=self.timer_mechanism.start_timer)
        self.start_button.grid(column=0, row=2)  

        self.reset_button = Button(self.root, text="Reset", highlightthickness=0, command=self.reset_mechanism.reset)
        self.reset_button.grid(column=2, row=2)      

        self.check_marks = Label(self.root, fg=GREEN, bg=YELLOW)
        self.check_marks.grid(column=1, row=3) 


    def update_timer_text(self, time_text):
        self.canvas.itemconfig(self.timer_text, text=time_text)

    def update_title(self, text, color):
        self.title_label.config(text=text, fg=color)

    def update_check_marks(self, marks):
        self.check_marks.config(text=marks)
 
    def run(self):
        self.root.mainloop()