# Players 1 and 2 enter pokemon types and whosever type is supereffective wins!

# import random for AI
import random

# Currently, only options are fire, water, grass.
pokemon_types = ["fire", "water", "grass"]

# initialize game tracker and scores
tracker = 1
score1 = 0
score2 = 0

while tracker < 6 and score1 < 3 and score2 < 3:
    print(f"Game {tracker}")
    # Player 1 chooses valid type
    player1 = input("Player 1, choose your starter type! \n").lower()
    while player1 not in pokemon_types:
        player1 = input("Player 1, choose a valid starter type! \n").lower()

    # no cheating space
    print("\n" * 100)

    # Player 2 chooses valid type or AI
    player2 = input("Player 2, choose your starter type or AI! \n").lower()
    while player2 not in pokemon_types and not "ai":
        player2 = input("Player 2, choose a valid option! \n").lower()

    if player2 == "ai":
        player2 = random.choice(pokemon_types)
        print(f"Player 2 chose {player2}")

    print("...")
    # outcome determined
    # Player1 choose fire
    if player1 == "fire":
        if player2 == "fire":
            print("A tie! Explosive!")
        elif player2 == "water":
            print("Washed away! Player 2 wins!")
            score2 += 1
        else:
            print("Brunt to a crisp! Player 1 wins")
            score1 += 1

    # Player 1 chooses water
    elif player1 == "water":
        if player2 == "fire":
            print("Washed away! Player 1 wins!")
            score1 += 1
        elif player2 == "water":
            print("A Tie! Blub blub!")
        else:
            print("Soaked up! Player 2 wins!")
            score2 += 1

    # Player 1 chooses grass
    else:
        if player2 == "fire":
            print("Brunt to a crisp! Player 2 wins")
            score2 += 1
        elif player2 == "water":
            print("Soaked up! Player 1 wins!")
            score1 += 1
        else:
            print("A tie! The grass is always greener!")
    print(f"Scores: \n Player 1: {score1} \n Player 2: {score2}")
    tracker += 1
if score1 > score2:
    print("And the winner is Player 1!")
elif score1 < score2:
    print("And the winner is Player 2!")
else:
    print("It's a draw!")
