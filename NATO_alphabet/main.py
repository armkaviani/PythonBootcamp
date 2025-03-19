from nato_phonetic import NatoAlphabet

def main():
    nato = NatoAlphabet("nato_phonetic_alphabet.csv")

    name = input("Enter a name: ")
    nato_words = nato.get_phonetic_name(name) 

    if nato_words:
        print(f"Phonetic code for {name.upper()}: {nato_words}")

if __name__ == "__main__":
    main()
