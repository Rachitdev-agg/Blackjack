import random
import art
from replit import clear

def game():
  Playing = False
  play = input("Do you want to play a game of blackjack? Type y or n: ")
  clear()
  if play == "y":
    Playing = True
    print(art.logo)
  limit = random.choice([15, 16, 17, 18])
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  computer_cards = [random.choice(cards), random.choice(cards)]
  player_cards = [random.choice(cards), random.choice(cards)]
  comp_score = sum(computer_cards)
  score = sum(player_cards)
  print(f"Your cards: {player_cards}, current score: {score}")
  print(f"Computer's first card: {computer_cards[0]}")
  while Playing == True:
    if comp_score == 21 and score == 21:
      print("Draw")
      game()
      Playing = False
    elif comp_score == 21:
      print("The computer has blackjack, You Lose")
      game()
      Playing = False
    elif score == 21:
      print("You have the backjack!! You WIN!!!")
      game()
      Playing = False
    while comp_score < limit:
      computer_cards.append(random.choice(cards))
      comp_score = sum(computer_cards)
    def more_cards():
      draw_not = input("Type y to get another card, type n to pass: ")
      if draw_not == "y":
        player_cards.append(random.choice(cards))
        score = sum(player_cards)
        print(f"Your cards: {player_cards}, current score: {score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if comp_score == 21 and score == 21:
          print(f"computer's cards: {computer_cards}, final score{comp_score}")
          print("Draw")
          game()
          Playing = False
        elif comp_score == 21:
          print(f"computer's cards: {computer_cards}, final score: {comp_score}")
          print("The computer has blackjack, You Lose")
          Playing = False
          game() 
        elif score == 21:
          print(f"computer's cards: {computer_cards}, final score: {comp_score}")
          print("You have the blackjack, You Win!!")
          Playing = False
          game()
        if comp_score > 21:
          m = -1
          for n in computer_cards:
            m += 1
            if n == 11:
              computer_cards[m] = 1
          if comp_score > 21:
            print(f"computer's cards: {computer_cards}, final score: {comp_score}")
            print("Opponent went over. You Win")
            game()
        elif score > 21:
          m = -1
          for n in player_cards:
            m += 1
            if n == 11:
              player_cards[m] = 1
          if score > 21:
            print(f"computer's cards: {computer_cards}, final score: {comp_score}")
            print("You went over. You lose")
            game()
        else:
          more_cards()
      elif draw_not == "n":
        score = sum(player_cards)
        print(f"Your cards: {player_cards}, final score: {score}") 
        print(f"computer's cards: {computer_cards}, final score: {comp_score}")
        if comp_score > 21:
          m = -1
          for n in computer_cards:
            m += 1
            if n == 11:
              computer_cards[m] = 1
          if comp_score > 21:
            print(f"computer's cards: {computer_cards}, final score: {comp_score}")
            print("Opponent went over. You Win")
            game()
        elif score > 21:
          m = -1
          for n in player_cards:
            m += 1
            if n == 11:
              player_cards[m] = 1
          if score > 21:
            print(f"computer's cards: {computer_cards}, final score: {comp_score}")
            print("You went over. You lose")
            game()
          else: 
            more_cards()
        elif comp_score > score:
          print(f"computer's cards: {computer_cards}, final score: {comp_score}")
          print("You lose")
          game()
        elif score > comp_score:
          print(f"computer's cards: {computer_cards}, final score: {comp_score}")
          print("You win")
          game()
    more_cards()  

game()
