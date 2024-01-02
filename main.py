import random
from ascii_art_blackjack import logo

def deal_the_cards():
    """Take a random card from the deck of cards"""  # doc string
    cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards_deck)
    return card


#  calculate the total sum of the cards of that list
def calculate_the_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Computer won ; because it has a score of BJ
    # Check for ace an 11 and if score is 21 then remove the 11 and replace it whit 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)  # remove ace with and replace 1
        cards.append(1)
    return sum(cards)

#  different stages of game play
def compare_player_vs_computer(score_of_user, score_of_computer):
    #   If you and the computer are both over, you lose.
    if score_of_user > 21 and score_of_computer > 21:
        return "You went over 21, You lose"

    if score_of_user == score_of_computer:
        return "Draw a card"
    elif score_of_computer == 0:
        return "Lose, computer has the Blackjack"
    elif score_of_user == 0:
        return "Nice you have a Blackjack"
    elif score_of_user >= 21:
        return "Sorry, you can't go higher than BlackJack"
    elif score_of_computer >= 21:
        return "You win, the computer bluffed"
    elif score_of_user >= score_of_computer:
        return "Congratulations, you win"
    else:
        return "Sorry, You lost the game"

# black jack game begins here
def play_blackjack():
    global computer_score
    print(logo)
    # create empty lists
    user_cards = []
    computer_cards = []
    over_and_out = False

    # deal the cards a put them in their lists
    for _var in range(2):  # run two loops
        user_cards.append(deal_the_cards())
        computer_cards.append(deal_the_cards())

    while not over_and_out:
        player_score = calculate_the_score(user_cards)
        computer_score = calculate_the_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {player_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            over_and_out = True  # End the game
        else:
            deal_again = input("Another card 'Y' or 'N' to pass : ")
        if deal_again == "Y":
            user_cards.append(deal_the_cards())
        else:
            over_and_out = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_the_cards())
        computer_score = calculate_the_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {player_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_player_vs_computer(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  # clear()
  play_blackjack()