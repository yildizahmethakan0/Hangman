import random
from words import word_list


chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

lives = 6

from ascii import logo

print(logo)

display = []
for _ in range(word_lenght):
    display += "_"


end_of_the_game = False

while not end_of_the_game:
    guess = input("guess a letter: ").lower()

    for position in range(word_lenght):
        letter = chosen_word[position]
        # print(
        #     f"Current position: {position}\n Current letter:{letter}\n Guessed letter: {guess}  "
        # )
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_the_game = True
            print("you lose")

    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_the_game = True
        print("You Win")

    from ascii import stages

    print(stages[lives])
