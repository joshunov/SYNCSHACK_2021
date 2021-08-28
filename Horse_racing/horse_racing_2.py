import pydealer as cd
from Horse_racing.horse_functions import *
from termcolor import colored


def horse_racing(player):
    SUITS = ["Hearts", "Diamonds", "Spades", "Clubs"]

    deck = cd.Deck(rebuild=True, re_shuffle=True)
    deck.shuffle()
    RACERS = ["Ace of Hearts", "Ace of Diamonds", "Ace of Spades", "Ace of Clubs"]
    deck.get_list(RACERS)
    in_play = []

    player_num = len(player)

    for i in range(player_num):
        bold_name = colored(player[i].name, attrs = ['bold'])

        try:
            player[i].bet = int(input(f"{bold_name}, how many drinks would you like to bet? "))
        except:
            bad_bet = True
            while bad_bet == True:
                new_bet = input(f"{bold_name}, you must enter a whole number: ")
                print("\n")
                try:
                    new_bet = int(new_bet)
                    player[i].bet = new_bet
                    break
                except:
                    continue
        print("\n\n")

        player[i].suit = input("On which suit (Hearts, Diamonds, Clubs, Spades)? ").lower().capitalize()
        print("\n\n")
        player_suit = True
        if player[i].suit not in SUITS:
            player_suit = False
            while player_suit != True:
                new_suit = input(f"{bold_name}, you must enter one of the following: Clubs, Diamonds, Hearts, Spades: ")
                new_suit = new_suit.lower().capitalize().strip()
                player[i].suit = new_suit
                if new_suit in SUITS:
                    break

        if player[i].suit not in in_play:
            in_play.append(player[i].suit)

    racer_dict = {"Ace of Hearts": 0, "Ace of Diamonds": 0, "Ace of Spades": 0, "Ace of Clubs": 0}

    counter = 0

    input("Press ENTER to start")

    while racer_dict[f"Ace of {in_play[0]}"] < 9 and racer_dict[f"Ace of {in_play[1]}"] < 9 and racer_dict[f"Ace of {in_play[-2]}"] < 9 and racer_dict[f"Ace of {in_play[-1]}"] < 9:
        card = deck.deal(1)
        print(colored(f"{card}\n", 'green', attrs = ['bold']))

        if card.cards[0].suit == "Hearts":
            racer_dict["Ace of Hearts"] += 1
        elif card.cards[0].suit == "Spades":
            racer_dict["Ace of Spades"] += 1
        elif card.cards[0].suit == "Diamonds":
            racer_dict["Ace of Diamonds"] += 1
        elif card.cards[0].suit == "Clubs":
            racer_dict["Ace of Clubs"] += 1


        for i in range(10):
            col = 0
            for key in racer_dict.keys():
                if racer_dict[key] == 9 - i:
                    print(f"|{SUITS[col]}|", end = "")
                else:
                    print("|********|", end='')
                col += 1   
            print("\n")
        
        print("\n\n\n")
        input("Press ENTER to turn the next card.")
        print("\n\n")

        if racer_dict["Ace of Hearts"] > counter and racer_dict["Ace of Spades"] > counter and racer_dict["Ace of Diamonds"] > counter and racer_dict["Ace of Clubs"] > counter:
            counter += 1
            input(f"All horses have reached {counter} points. Which horse will fall one point behind? (press ENTER)\n")
            reverse = deck.deal(1)
            print(colored(f"{reverse}\n", 'red', attrs= ['bold']))
        

            if reverse.cards[0].suit == "Hearts":
                racer_dict["Ace of Hearts"] -= 1
            elif reverse.cards[0].suit == "Spades":
                racer_dict["Ace of Spades"] -= 1
            elif reverse.cards[0].suit == "Diamonds":
                racer_dict["Ace of Diamonds"] -= 1
            elif reverse.cards[0].suit == "Clubs":
                racer_dict["Ace of Clubs"] -= 1

            for i in range(10):
                col = 0
                for key in racer_dict.keys():
                    if racer_dict[key] == 9 - i:
                        print(f"|{SUITS[col]}|", end="")
                    else:
                        print("|********|", end='')
                    col += 1
                print("\n")

            print("\n\n\n")
            input("Press ENTER to turn the next card.")
            print("\n\n")


    for key in racer_dict.keys():
        if racer_dict[key] == 9:
            winning_card = key


    winning_players = []
    for i in range(player_num):
        if player[i].suit in winning_card:
            winning_players.append(player[i].name)

    print("Congratumalations to the winners:")
    for name in winning_players:
        print(colored(f"{name}\n", 'yellow', attrs= ['bold']))

    print("Now for all you losers who don't know how to punt, lets see how much you have to drink:\n")
    for i in range(player_num):
        if player[i].name in winning_players:
            bold_name = colored(f"{player[i].name}", 'yellow', attrs= ['bold'])
            bold_sips = colored(f"{player[i].bet}", attrs= ['bold'])
            print(f"{bold_name}, you get to dish out {player[i].bet * 2} sips! Good job\n")
        else:
            bold_name = colored(f"{player[i].name}", 'red', attrs= ['bold'])
            bold_sips = colored(f"{player[i].bet}", attrs= ['bold'])
            print(f"{bold_name}, you gotta pick up your game. Drink {bold_sips} sips\n")
            for j in range(player[i].bet):
                player[i].drink()
        





    

