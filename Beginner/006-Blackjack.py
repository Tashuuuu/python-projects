import random

your_cards = []
com_cards = []

def deal_cards():
  cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
  card = random.choice(cards)
  return card

def result(a, b):
  user_total_sum = sum(your_cards) % 21
  com_total_sum = sum(com_cards) % 21
  if ((user_total_sum == 0) or (com_total_sum > 21) or (user_total_sum > com_total_sum)):
    print("Yay! You win with a Blackjack")
  elif ((com_total_sum == 0) or (user_total_sum > 21) or (user_total_sum < com_total_sum)):
    print("You lost, computer has Blackjack")
  else:
    print("Draw")

while (True):
  start = input("Let's start blackjack, shall we? [y/n]: ")
  if (start == "y"):
    your_cards.extend((deal_cards(), deal_cards()))
    com_cards.extend((deal_cards(), deal_cards()))
    print(f"Your cards are: {your_cards}, current score: {sum(your_cards)}")
    print(f"Computer's first card: {com_cards[0]}")
    next = input("To get more cards type 'y', type 'n' to pass: ")
    if (next == 'y'):
      your_cards.append(deal_cards())
      com_cards.extend((deal_cards(), deal_cards()))
      print(f"Your cards are: {your_cards}, current score: {sum(your_cards)}")
      print(f"Computer's first card: {com_cards[0]}")
      next = input("To get more cards type 'y', type 'n' to pass: ")
      if (next == 'y'):
        your_cards.append(deal_cards())
        com_cards.extend((deal_cards(), deal_cards()))
        print(f"Your cards are: {your_cards}, current score: {sum(your_cards)}")
        print(f"Computer's first card: {com_cards[0]}")
        next = input("To get more cards type 'y', type 'n' to pass: ")
        if (next == 'y'):
          your_cards.append(deal_cards())
          com_cards.extend((deal_cards(), deal_cards()))
          print(f"Your cards are: {your_cards}, current score: {sum(your_cards)}")
          print(f"Computer's first card: {com_cards[0]}")
          next = input("To get more cards type 'y', type 'n' to pass: ")  

    print(f"Your final hand: {your_cards}, final score: {sum(your_cards)}")
    print(f"Computer's final hand: {com_cards}, final score: {sum(com_cards)}")
    result(your_cards, com_cards)
    play_again = input("Do you want to play again? [y/n]: ")
    if play_again == "y":
      continue
    else:
      break
  elif (start == "n"):
    break
  else:
    print("Please enter either 'y' or 'n' for 'yes' or 'no'.")
    continue
