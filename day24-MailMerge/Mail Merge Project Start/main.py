# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt", mode= "r") as f:
    letter = f.read()
with open("./Input/Names/invited_names.txt", mode="r") as f:
    while True:
        name = f.readline().strip("\n")
        letter_with_name = letter.replace("[name]", name, 1)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode= 'w') as f2:
            f2.write(letter_with_name)
        if not name:
            break
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
