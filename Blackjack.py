import random

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_scores, computer_scores):
    if user_scores == computer_scores:
        return "Draw "
    elif computer_scores == 0:
        return "lose, opponent has blackjack"
    elif user_scores == 0:
        return "win with a blackjack"
    elif user_scores > 21:
        return "you went over. you lose"
    elif computer_scores > 21:
        return "you went over. you win"
    elif user_scores > computer_scores:
        return " you win"
    elif user_scores < computer_scores:
        return " you lose"


user_cards = []
computer_cards = []
computer_score = -1
user_score = -1
for _ in range(2):
    new_card = deal_cards()
    user_cards.append(new_card)
    computer_cards.append(deal_cards())
    is_game_over = False
while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Compter's first card :  {computer_cards[0]}")
    if user_score == 0 or computer_score == 0  or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == 'y':
            user_cards.append(deal_cards())
        else:
            is_game_over = True

while computer_score !=0 and computer_score < 17:
    computer_cards.append(deal_cards())
    computer_score = calculate_score(computer_cards)

print(f"your final hand : {user_cards}, final score: {user_score}")
print(f"computer's final hand : {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))



