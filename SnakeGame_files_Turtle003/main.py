#TODO: Create a letter using starting_letter.txt 

PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_leter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_leter)

