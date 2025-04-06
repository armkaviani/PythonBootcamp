from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizeInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.frame = Tk()
        self.frame.title("Quizzler")
        self.frame.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_board = Label(text="Score: 0", bg=THEME_COLOR, fg="White")
        self.score_board.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_img, command=self.get_true_answer)
        self.false_button = Button(image=self.false_img, command=self.get_false_answer)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.get_true_answer()
        self.get_false_answer()

        self.frame.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question_text)


    def get_true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def get_false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback(self, is_right):
        if is_right is True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.frame.after(1000, self.get_next_question)

        
        
        