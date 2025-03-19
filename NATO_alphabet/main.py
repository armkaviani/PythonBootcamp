from nato_phonetic import NatoAlphabet

def main():
    nato = NatoAlphabet("nato_phonetic_alphabet.csv")

    name = input("Enter a name: ")
    nato_words = nato.get_phonetic_name(name) 

    