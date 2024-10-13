#step  01: create one function to give random card numbers as output

import random


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


#step 02:create a function  calculate_score() to calculate the score of the cards , which will take the list of cards as input and returns sum/score

#step 03:check for the blackjack , a hand with only 2 cards and a sum of 21

#step 04:check for an ace(11) , if the score is already over 21 ,remove the 11 and replace it with 1


def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)


def compare(u_Score, c_Score):
  if u_Score == c_Score:
    return "draw"
  elif c_Score == 0:
    return "Loose, oppponent has blackjack"
  elif u_Score == 0:
    return "Win with a blackjack"
  elif user_score > 21:
    return "You went over .You loose"
  elif c_Score > 21:
    return "Opponent went over . You win"
  elif u_Score > c_Score:
    return "You win"
  else:
    return "You loose"


#step 05: deal 2 cards for user and for computer
user_cards = []
computer_cards = []
is_game_over = False
for fillingCards in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

#step 06:call the function calculate_score() ,if the computer or the user has a blackjack or if the users score is above 21 the game ends
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

while not is_game_over:
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  print(f"your cards :{user_cards} , current score :{user_score}")
  print(
      f"computer's first card:{computer_cards[0]},computer's current score:{computer_score}"
  )

  if user_score == 0 or user_score > 21:
    is_game_over = True
  else:
    user_should_deal = input("Type y to get another card , type n to pass : ")
    if user_should_deal == "y":
      user_cards.append(deal_card())
    else:
      is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(compare(user_score, computer_score))
