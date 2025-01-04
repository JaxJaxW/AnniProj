import random

from orca.debug import printMessage

print("START GAME #1")


card = random.randrange(1,13)

#print(card)

cards = ["ACE", "2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK", "QUEEN", "KING"]
#           0    1    2    3    4    5    6   7     8    9     10       11        12

playerpoints = 0

print("Your card is a", cards[card-1], "!")


# Add card to the player's points
if card > 10:
    playerpoints += 10
else:
    playerpoints += card

print("Your hand is:", playerpoints)

game = True



while game:

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
            playerpoints += 10
        else:
            playerpoints += card

        print("Your card is a", cards[card - 1], "!")
        print("Your hand is:", playerpoints)

    elif prompt == "2":
        pass

    elif prompt == "3":
        pass

    elif prompt == "4":
        game = False

    else:
        print("Invalid input!")
        print("Please enter an integer value between 1 and 4.")