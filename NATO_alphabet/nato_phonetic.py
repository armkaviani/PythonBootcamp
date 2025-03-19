import pandas as pd

class NatoAlphabet:
    def __init__(self, csv_file):
        
        self.nato_alphabet = pd.read_csv(csv_file)
        self.nato_alphabet_dict = {row.letter: row.code for (index, row) in self.nato_alphabet.iterrows()}

    def get_phonetic_name(self, name):
        phonetic_name = [self.nato_alphabet_dict[letter] for letter in name.upper()]
        return phonetic_name
