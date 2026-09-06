with open("Input/letters/starting_letter.txt", mode="r") as file:
    letter = file.read()

with open("Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()

for name in names:
    clean_name = name.strip()

    personalized_letter = letter.replace("[name]", clean_name)

    with open(
        f"Output/ReadyToSend/{clean_name}.txt",
        mode="w"
    ) as ready:
        ready.write(personalized_letter)