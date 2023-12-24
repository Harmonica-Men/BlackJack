import random


def deal_the_cards():
    """Take a random card from the deck of cards"""
    cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards_deck)
    return card


user_cards = []
computer_cards = []

# deal the cards a put them in there lists
for  _var in range(2):
    user_cards.append(deal_the_cards())
    computer_cards.append(deal_the_cards())

