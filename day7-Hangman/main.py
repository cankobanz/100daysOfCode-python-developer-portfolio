import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for i in range(0, len(chosen_word)):
    display.append("_")

won = False
lives = 6
while not won and lives != 0:
    won = True
    found = False
    guess = input("Guess a letter: ").lower()

    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter
            found = True
        if '_' in display:
            won = False

    if not found:
        lives -= 1
        print(stages[lives])
    else:
        print(stages[lives])

    print(f"{' '.join(display)}")

if won:
    print("Congrats! You won!")
if lives == 0:
    print(":(")
