import random

class FlashcardGame:
    def __init__(self, flashcard_data, flashcard_ui):
        self.flashcard_data = flashcard_data
        self.flashcard_ui = flashcard_ui
        self.data_random = {}
        self.flip_timer = self.flashcard_ui.frame.after(3000, self.flip_card)

    def random_card(self):
        self.flashcard_ui.frame.after_cancel(self.flip_timer)
        self.data_random = random.choice(self.flashcard_data.data_dic)
        self.flashcard_ui.update_card("French", self.data_random["French"], self.flashcard_ui.card_front_image)
        self.flip_timer = self.flashcard_ui.frame.after(3000, self.flip_card)

    def flip_card(self):
        self.flashcard_ui.update_card("English", self.data_random["English"], self.flashcard_ui.card_back_image)

    def is_correct(self):
        self.flashcard_data.remove_word(self.data_random)
        self.random_card()