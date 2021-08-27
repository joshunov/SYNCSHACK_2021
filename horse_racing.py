from deck_of_cards import deck_of_cards as dc

deck_obj = dc.DeckOfCards

for i in range(52):
    card = deck_obj.give_random_card
    print(card)