import random


def deal_the_cards():
    """Take a random card from the deck of cards"""  # doc string
    cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards_deck)
    return card


#  calculate the total sum of the cards of that list
def calculate_the_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Computer won ; because it has a score of BJ
    # Check for ace an 11 and if score is 21 then remove the 11 and replace it whit 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)  # remove ace with and replace 1
        cards.append(1)
    return sum(cards)


#  different stages of game play
def compare_player_vs_computer(userscore, computerscore):
  #   If you and the computer are both over, you lose.
    if userscore > 21 and computerscore > 21:
        return "You went over. You lose"

    if userscore == computerscore:
        return "Draw a card"
    elif computerscore == 0:
        return "Lose, computer has the Blackjack"
    elif userscore == 0:
        return "Nice you have a Blackjack"
    elif userscore >= 21:
        return "Sorry, you can't go higher than BlackJack"
    elif computerscore >= 21:
        return "You win, the computer bluffed"
    elif userscore >= computerscore:
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

# print the score of player and computer
print(f" last card: {user_cards}, final score: {player_score}")
print(f" computer last card; {computer_cards}, final score : {computer_score}")
print(compare_player_vs_computer(player_score, computer_score))
