import pydealer as cd


class Player:
    def __init__(self):
        self.name = "John"
        self.drinks = 0
        self.suit = "Diamonds"

    def create(self):
        self.name = input("What is your name? ")
        self.drinks = input("How many drinks would you like to bet? ")
        self.suit = input("On which suit? ")

        

deck = cd.Deck(rebuild = True, re_shuffle = True)
deck.shuffle()

RACERS = ["Ace of Hearts", "Ace of Diamonds", "Ace of Spades", "Ace of Clubs"]

deck.get_list(RACERS)

print("dun da da da DAAA!!\nWelcome to the Horse Races!\nThe rules of this game are very simple:")
print("You should each place a bet on a suit in a deck of cards: Hearts, Diamonds, Spades, Clubs")
print("The bets will be made in drinks, for example, I could bet 3 drinks (sips)")
print("Cards will be dealt from the deck and the suit of the card will determine which horse advances")
print("The track is 8 points long so the horse which first reaches 9 points wins!!")
print("If your horse didn't win, you must drink the amount of drinks you placed as a bet (that would mean I drink 3 sips)")
print("Those who bet on the winning horse get to hand out double the ammount they bet on (I could hand out 6 drinks)")
print("Each time all the horses have advanced to a at least one more point, a card will be dealt which moves the horse of that suit BACK")
print("Happy punting, drink responsibly")

num_play = int(input("How many players? "))


# players = {}
# for i in range(num_play):
#     bet = input("player name: ")
#     players[name] = 0

# for key in players.keys():
#     bet = int(input(f"{key}, how many drinks would you like to bet? "))
#     players[key] = bet