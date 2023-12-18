import random
from hangman_art import logo
from hangman_art import stages
from words import word_list

print(logo)

blanks = []
end_game = False
lives = 6

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

for _ in chosen_word:
    blanks += '_'

print(blanks)

while not end_game:
    player_guess = input('Guess a letter\n').lower()

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == player_guess:
            blanks[position] = letter
    if player_guess not in blanks:
        lives -= 1
        if lives == 0:
            end_game = True
            print('You lose!')
            print(f'Word was {chosen_word}')
    print(f"{blanks}")
    if '_' not in blanks:
        end_game = True
        print('You Win')
    print(stages[lives])


