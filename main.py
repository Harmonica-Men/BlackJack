import random


def deal_the_cards():
    """Take a random card from the deck of cards"""  # doc string
    cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards_deck)
    return card


#  calculate the total sum of the cards of that list
def calculate_the_score(cards_deck):
    if sum(cards_deck) == 21 and len(cards_deck) == 2:
        return 0  # Computer won ; because it has a score of BJ
    # Check for ace an 11 and if score is 21 then remove the 11 and replace it whit 1
    if 11 in cards_deck and sum(cards_deck) > 21:
        cards_deck.remove(11)  # remove ace with and replace 1
        cards_deck.append(1)
    return sum(cards_deck)


# create empty lists
user_cards = []
computer_cards = []

# deal the cards a put them in their lists
for _var in range(2):  # run two loops
    user_cards.append(deal_the_cards())
    computer_cards.append(deal_the_cards())

player_score = calculate_the_score(user_cards)
computer_score = calculate_the_score(computer_cards)
print(f" player: {user_cards}, current score {player_score}")
print(f" computer top card of the deck: {computer_cards[0]}")

if player_score == 0 or computer_score == 0 or player_score > 21:
    over_and_out = True  # End the game
