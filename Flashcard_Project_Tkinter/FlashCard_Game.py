class FlashcardGame:
    def __init__(self, flashcard_data, flashcard_ui):
        self.flashcard_data = flashcard_data
        self.flashcard_ui = flashcard_ui
        self.data_random = {}
        self.flip_timer = self.flashcard_ui.frame.after(3000, self.flip_card)