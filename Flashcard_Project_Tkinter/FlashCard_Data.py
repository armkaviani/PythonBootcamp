import pandas as pd


class FlashcardData:
    def __init__(self):
        self.data_dic = []
        self.load_data()

    def load_data(self):
        try:
            data = pd.read_csv("french_words.csv")
        except FileNotFoundError:
            original_data = pd.read_csv("data/french_words.csv")
            self.data_dic = original_data.to_dict(orient='records')
        else:
            self.data_dic = data.to_dict(orient="records")

    def remove_word(self, word):
        self.data_dic.remove(word)
        data = pd.DataFrame(self.data_dic)
        data.to_csv("words_to_learn.csv", index=False)



