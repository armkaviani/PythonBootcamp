from tkinter import *


class FlashcardUI:
    def __init__(self, frame, flashcard_game):
        self.frame = frame
        self.flashcard_game = flashcard_game
        self.canvas = Canvas(width=800, height=526)
        self.card_front_image = PhotoImage(file="images/card_front.png")
        self.card_back_image = PhotoImage(file="images/card_back.png")
        self.card_background = self.canvas.create_image(400, 263, image=self.card_front_image)
        self.title_card = self.canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
        self.word_card = self.canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
        self.canvas.config(bg="#B1DDC6", highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.right_button_img = PhotoImage(file="images/right.png")
        self.check_button = Button(image=self.right_button_img, highlightthickness=0, command=self.flashcard_game.is_correct)
        self.check_button.grid(row=1, column=1)

        self.wrong_button_img = PhotoImage(file="images/wrong.png")
        self.unknown_button = Button(image=self.wrong_button_img, highlightthickness=0, command=self.flashcard_game.random_card)
        self.unknown_button.grid(row=1, column=0)

    def update_card(self, title, word, image):
        self.canvas.itemconfig(self.title_card, text=title, fill="black" if title == "French" else "white")
        self.canvas.itemconfig(self.word_card, text=word, fill="black" if title == "French" else "white")
        self.canvas.itemconfig(self.card_background, image=image)