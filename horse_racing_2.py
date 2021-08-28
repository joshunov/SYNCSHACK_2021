import pydealer as cd
from Main import *
from horse_functions import *

def horse_racing(players: Game.player_list):

    deck = cd.Deck(rebuild=True, re_shuffle=True)
    deck.shuffle()
    RACERS = ["Ace of Hearts", "Ace of Diamonds", "Ace of Spades", "Ace of Clubs"]
    deck.get_list(RACERS)

    player_num = len(players)

    for i in range(player_num):
        player[i].bet = input(f"{player[i].name}, how many drinks would you like to bet?\n")
        player[i].suit = input("On which suit?\n")

    racer_dict = {"Ace of Hearts": 0, "Ace of Diamonds": 0, "Ace of Spades": 0, "Ace of Clubs": 0}

    counter = 0

    while racer_dict["Ace of Hearts"] < 10 and racer_dict["Ace of Spades"] < 10 and racer_dict["Ace of Diamonds"] < 10 and racer_dict["Ace of Clubs"] < 10:
        card = deck.deal(1)
        print(card)

        if card.cards[0].suit == "Hearts":
            racer_dict["Ace of Hearts"] += 1
        elif card.cards[0].suit == "Spades":
            racer_dict["Ace of Spades"] += 1
        elif card.cards[0].suit == "Diamonds":
            racer_dict["Ace of Diamonds"] += 1
        elif card.cards[0].suit == "Clubs":
            racer_dict["Ace of Clubs"] += 1

        if racer_dict["Ace of Hearts"] > counter and racer_dict["Ace of Spades"] > counter and racer_dict["Ace of Diamonds"] > counter and racer_dict["Ace of Clubs"] > counter:
            print(f"All horses have reached {counter} points. Which horse will fall one point behind?\n")
            reverse = deck.deal(1)
            print(f"{reverse}\n")

            if reverse.cards[0].suit == "Hearts":
                racer_dict["Ace of Hearts"] -= 1
            elif reverse.cards[0].suit == "Spades":
                racer_dict["Ace of Spades"] -= 1
            elif reverse.cards[0].suit == "Diamonds":
                racer_dict["Ace of Diamonds"] -= 1
            elif reverse.cards[0].suit == "Clubs":
                racer_dict["Ace of Clubs"] -= 1

    
    winning_card = winning_horse(racer_dict)

    winning_players = []
    for i in range(player_num):
        if player[i].suit == winning_card:
            winning_players.append(player[i].name)

    


        


    

