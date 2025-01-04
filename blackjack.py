"""
Fun Blanchard game of BlackJack, gator edition
"""

import random



print("START GAME #1")


card = random.randrange(1,13)

#print(card)

cards = ["ACE", "2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK", "QUEEN", "KING"]
#           0    1    2    3    4    5    6   7     8    9     10       11        12

PLAYERS_HAND = 0

print("Your card is a", cards[card-1], "!")


# Add card to the player's points
if card > 10:
    PLAYERS_HAND += 10
else:
    PLAYERS_HAND += card

print("Your hand is:", PLAYERS_HAND)

GAME = True



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
            PLAYERS_HAND += 10
        else:
            PLAYERS_HAND += card

        print(f"Your card is a {cards[card-1]}!")
        print("Your hand is:", PLAYERS_HAND)

        if players_hand > 21:
            print("You exceeded 21! You lose.")
        if players_hand == 21:
            print ("BLACKJACK! You win!")

        if playerpoints > 21:
            print("You exceeded 21! You lose.")
        if PLAYERS_HAND == 21:
            print ("BLACKJACK! You win!")

    elif prompt == "2":
        dealers_hand = random.randrange(16, 26)

        if dealers_hand > 21:
            print("You win!")
        elif dealers_hand == PLAYERS_HAND:
            print("It's a tie! No one wins!")
        elif PLAYERS_HAND > dealers_hand:
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
