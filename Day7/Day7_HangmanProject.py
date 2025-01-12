import random
stages = [
    '''   -----
   |   |
       |
       |
       |
       |
  ========''',

    '''   -----
   |   |
   O   |
       |
       |
       |
  ========''',

    '''   -----
   |   |
   O   |
   |   |
       |
       |
  ========''',

    '''   -----
   |   |
   O   |
  /|   |
       |
       |
  ========''',

    '''   -----
   |   |
   O   |
  /|\  |
       |
       |
  ========''',

    '''   -----
   |   |
   O   |
  /|\  |
  /    |
       |
  ========''',

    '''   -----
   |   |
   O   |
  /|\  |
  / \  |
       |
  ========'''
]

lives = 0

random_list = ['monkey', 'ferrari', 'cabbage', 'tiger']
# TODO-1 - Randomly choose a word from the word-list and assign it to any variable
chosen_word = random.choice(random_list)
print(chosen_word)

# Create a placeholder with the same number of blanks as the chosen_word
placeholder = ""
for position in range(0, len(chosen_word) + 1):
    placeholder += "_"
print(placeholder)

# TODO-2 : Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
game_over = False
correct_letters = []
i = 1
while not game_over:
    guess = input('Guess any letter: ').lower()
# print(guess)
# Create a "display" that puts the guess letter in the right positions and _
    display = ""

# TODO-3: Check if the letter the user guessed(guess) is one of the letters in the chosen_word. Print 'Right' if it,
#  'Wrong' if it's not.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives += 1
        if lives == 7:
            game_over = True
            print("********You lose********")

    if "_" not in display:
        game_over = True
        print("********You win********")
    # Print the ascii art from 'stages' that corresponds to the current number of 'lives' the user has remaiining.
    print(stages[lives])
