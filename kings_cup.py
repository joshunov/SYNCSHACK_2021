# from Main import *
import random

def run_kings(playerlist):
    playerNum = len(playerlist)

    cardCount = {
        "Ace": 4,
        "King": 4,
        "Queen": 4,
        "Jack": 4,
        "10": 4,
        "9": 4,
        "8": 4,
        "7": 4,
        "6": 4,
        "5": 4,
        "4": 4,
        "3": 4,
        "2": 4,        
    }

    currentPlayerIndex = 0
    gameOver = False

    while True:
        currentPlayer = playerlist[currentPlayerIndex].name

        print("\n---------------------------------------------\n")
        input("It's {}'s turn. Press ENTER to continue.\n".format(currentPlayer))

        card = random.choice(list(cardCount.keys()))
        print("{} has pulled the card \"{}\" - ".format(currentPlayer, card), end=" ")
        cardCount, gameOver = ActionCardOutcome(currentPlayer, card, cardCount)

        if gameOver < 0:
            break

        input("\nPress ENTER to continue, once the task is finished!")

        currentPlayerIndex += 1

        if currentPlayerIndex == playerNum:
            currentPlayerIndex = 0

    print("\nYou have finished King's cup - returning you to the main menu!")

    return 1


def ActionCardOutcome(player, cardOutcome, remainingDeck):
    gameFinished = False

    if cardOutcome == "Ace":
        print("Waterfall!")
        print("Everyone drinks, starting with {}.".format(player))
    elif cardOutcome == "King":
        if remainingDeck[cardOutcome] == 1:
            print("{} has pulled the last king! They must finish the King's Cup!".format(player))
            input("Press ENTER when complete!")
            gameFinished = True
        else:
            print("{} must pour some of their drink into the cup.".format(player))
            print("There are {} King(s) remaining.".format(remainingDeck[cardOutcome] - 1))
    elif cardOutcome == "Queen":
        print("{} is the new Question Master!".format(player))
    elif cardOutcome == "Jack":
        print("Never Have I Ever!")
        print("Loser of this one drinks.")
    elif cardOutcome == "10":
        print("Categories!")
        print("{} picks a category, others need to say things in that category. First to not be able to drinks.".format(player))
    elif cardOutcome == "9":
        print("Bust a Rhyme!")
        print("Pick a word, others must rhyme it. First to not be able to drinks.")
    elif cardOutcome == "8":
        print("Mate!")
        print("{} - find a drinking buddy. You both drink together for the remainder of the game.".format(player))
    elif cardOutcome == "7":
        print("Heaven!")
        print("Reach for the sky; last person drinks.")
    elif cardOutcome == "6":
        print("Dicks!")
        print("All the guys drink.")
    elif cardOutcome == "5":
        print("Bust a jive!")
        print("Create a dance move; the one who screws it up drinks.")
    elif cardOutcome == "4":
        print("Whores!")
        print("Ladies drink.")
    elif cardOutcome == "3":
        print("Me")
        print("{} takes two drinks.".format(player))
    elif cardOutcome == "2":
        print("You!")
        print("{} gets to pick someone to take two drinks.".format(player))

    remainingDeck[cardOutcome] -= 1

    if remainingDeck[cardOutcome] == 0:
        remainingDeck.pop(cardOutcome)

    if gameFinished == True:
        return remainingDeck, -1
    else:
        return remainingDeck, 0


if __name__ == "__main__":
    run_kings(["Jordan", "Josh", "Adam", "Cam", "Rishi", "Hamish"])