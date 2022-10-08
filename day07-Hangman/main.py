import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
chosen_word = random.choice(word_list)

# Comment it if you want to real game.
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(len(chosen_word)):
    display += "_"

end_of_game = False
lives = 6
while not end_of_game and lives != 0:
    found = False
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You wrote same letter!")
        continue

    #Check guessed letter
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Check if user has got all letters.
    if '_' not in display:
        end_of_game = True
        print("Congrats! You won!")

    print(stages[lives])
    print(f"{' '.join(display)}")
