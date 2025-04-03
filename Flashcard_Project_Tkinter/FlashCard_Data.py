import pandas as pd


class FlashcardData:
    def __init__(self):
        self.data_dic = []
        self.load_data()

    def load_data(self):
        """Load data from CSV file and handle file not found error"""
        try:
            data = pd.read_csv("french_words.csv")
        except FileNotFoundError:
            original_data = pd.read_csv("data/french_words.csv")
            self.data_dic = original_data.to_dict(orient='records')
        else:
            self.data_dic = data.to_dict(orient="records")
