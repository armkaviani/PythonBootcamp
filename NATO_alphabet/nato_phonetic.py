import pandas as pd

class NatoAlphabet:
    def __init__(self, csv_file):
        
        self.nato_alphabet = pd.read_csv(csv_file)
