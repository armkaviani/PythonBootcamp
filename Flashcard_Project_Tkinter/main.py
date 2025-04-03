from tkinter import *
from FlashCard_Data import FlashcardData
from FlashCard_Game import FlashcardGame
from FlashCard_UI import FlashcardUI


def main():
    frame = Tk()
    frame.title("Flashy")
    frame.config(padx=50, pady=50, bg="#B1DDC6")

    flashcard_data = FlashcardData()  # Initialize the data
    flashcard_ui = FlashcardUI(frame, None)  # Initialize the UI without the game initially

    flashcard_game = FlashcardGame(flashcard_data, flashcard_ui)  # Initialize the game

    flashcard_ui.flashcard_game = flashcard_game  # Now assign the game to the UI

    flashcard_game.random_card()  # Start the game by showing the first card
    frame.mainloop()  # Start the Tkinter event loop


if __name__ == "__main__":
    main()