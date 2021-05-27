"""
Classic Hangman game.

Can take user input for term/phrase to be guessed or provides a 
word from a limited pool of options.
"""


from random import choice
from os import system


# Declare game variables
words = ['fortnite', 'chess', 'coding', 'apple', 'beach', 'raptor']
game_over = False


def hangman():
    # provides mechanics to play game.
    global game_over
    personal = input(
        "Would you like to provide your own answer for others to guess? (y/n) ")
    if personal == "y" or personal == "yes":
        word = input(
            "Please choose something for the other players to guess: ")
        hidden_word = []
        for char in word:
            if char == " ":
                hidden_word.append(" ")
            else:
                hidden_word.append("_")
        system("clear")

    else:
        # randomly chooses a word from words list and it becomes the word the user tries to guess
        word = choice(words)
        words.remove(word)
        # Creates underscores of the length of word for user to visualize the word and fills when guessed correctly.
        hidden_word = ["_"] * len(word)
    guessed, lives, try_again = [], min(7, len(word)), None

    while game_over is False:
        print(f"Guessed letters: {guessed}")
        print(f"Word to guess: {''.join(hidden_word)}")
        print(f"Remaining lives: {lives}")
        if hidden_word == word:
            print("You win!")
            if len(words) > 0:
                play_again()
            else:
                print("I'm all out of words. Game completed!")
                game_over == True
                break
        ans = input("Guess a letter (or type 'quit'): ").lower().strip()
        system("clear")
        if ans == "quit":
            print("Thanks for playing!")
            game_over = True
            break
        elif ans == word:
            print(word)
            print("Congratulations, you got it!")
            play_again()
        elif len(ans) != 1:
            print("Please type only one letter at a time.")
        elif ans not in "abcdefghijklmnopqrstuvwxyz":
            print('Please type a single letter.')
        elif ans in word and ans not in guessed:  # check if letter in word
            print("You guessed correctly!")
            guessed.append(ans)
            # create a loop to change underscore to proper letter
            for i in range(len(word)):
                if word[i] == ans:  # Compares values at indexes
                    hidden_word[i] = ans
            if word == ''.join(hidden_word):
                print("Congratulations, you found the answer!")
                play_again()
        elif ans in guessed:
            print("You already guessed that. Try again.")
        else:
            lives -= 1
            print("Incorrect. You lost a life.")
            guessed.append(ans)  # adds ans to guessed list
            if lives == 0:
                print("You lost all your lives. Game over!")
                play_again()


def play_again():
    # determines whether to play another round or end game.
    global game_over
    global words
    try_again = None
    while try_again not in ("yes", 'y', 'n', 'no'):
        try_again = input("Play Again? (y/n) ").lower().strip()
    if try_again == "y" or try_again == "yes":
        system("clear")
        hangman()
    else:
        print('Thanks for playing!')
        game_over = True


system("clear")
hangman()
