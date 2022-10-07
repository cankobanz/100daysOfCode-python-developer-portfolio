from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, given_direction):
    if given_direction == "decode":
        shift_amount *= -1

    encrypted_text = ""
    for i, letter in enumerate(plain_text):
        # Keep non-letter character as it is, encrypt otherwise.
        if letter.isalpha():
            new_index = (alphabet.index(letter) + shift_amount) % 26
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += letter
    print(f"The encoded text is {encrypted_text}")


print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(text, shift, direction)

restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
if restart == "no":
    should_end = True
    print("Goodbye")
