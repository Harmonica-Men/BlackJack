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

def compare_player_vs_computer(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose"

  if user_score == computer_score:
    return "Draw a card"
  elif computer_score == 0:
    return "Lose, computer has the Blackjack"
  elif user_score == 0:
    return "Nice you have a Blackjack"
  elif user_score > 21:
    return "Sorry, you can't go higher than BlackJack"
  elif computer_score > 21:
    return "You win, the computer bluffed"
  elif user_score > computer_score:
    return "Congratulations, you won"
  else:
    return "Sorry, You lost the game"


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
else:
    deal_again = input("Another card 'Y' or 'N' to pass")
    if deal_again == "Yes":
        user_cards.append(deal_the_cards())
    else:
        over_and_out = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_the_cards())
    computer_score = calculate_the_score(computer_cards)

