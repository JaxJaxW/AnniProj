"""
Fun Blanchard game of BlackJack, gator edition
"""

import random

GAME = True
CARDS = ["ACE", "2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK", "QUEEN", "KING"]
game_number = 1
players_hand = 0

print(f"START GAME #{game_number}")
print("")

card = random.randrange(1,13)

print(f"Your card is a {CARDS[card - 1]}!")


# Add card to the player's points
if card > 10:
    players_hand += 10
else:
    players_hand += card

print("Your hand is:", players_hand)

while GAME:

    print("")
    print("1. Get another card")
    print("2. Hold hand")
    print("3. Print statistics")
    print("4. Exit")
    print("")
    prompt = input("Choose an option: ")

    if prompt == "1":
        card = random.randrange(1, 13)
        if card > 10:
            players_hand += 10
        else:
            players_hand += card

        print(f"Your card is a {CARDS[card - 1]}!")
        print("Your hand is:", players_hand)

        if players_hand > 21:
            print("You exceeded 21! You lose.")
        if players_hand == 21:
            print ("BLACKJACK! You win!")

    elif prompt == "2":
        dealers_hand = random.randrange(16, 26)

        if dealers_hand > 21:
            print("You win!")
        elif dealers_hand == players_hand:
            print("It's a tie! No one wins!")
        elif players_hand > dealers_hand:
            print("Dealer wins!")
        else:
            print("You win!")

    elif prompt == "3":
        pass

    elif prompt == "4":
        GAME = False

    else:
        print("Invalid input!")
        print("Please enter an integer value between 1 and 4.")
