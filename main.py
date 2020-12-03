########Guess the Number#########

from art import logo
from random import choice
from os import system
number_list = []

def select_random(num_list):
  for number in range(1, 101):
    num_list.append(number)
  return choice(num_list)

def select_mode(user_direction):
  if user_direction == 'easy':
    lives = 10
    return lives
  elif user_direction == 'hard':
    lives = 5
    return lives
  else:
    return None

def run():
  print(f"""
  {logo}
  Hello! This is a number guessing game
  --------Rules------
  1. I'll be picking a number from 1-100
  2. You have to guess it
  3. Enjoy! 
    """)
  user_mode = input("What mode do you want to play the game in? (easy/hard)").lower()
  lives = select_mode(user_mode)
  print(f"Okay, since you chose {user_mode}, you have {lives} lives in total")
  computer_choice = select_random(number_list)
  print("""
Okay, I'm thinking of a number
  """)
  while True:
    user_choice = int(input("Guess my number: "))
    if user_choice == computer_choice:
      print("Good Job! U won!")
      break
    elif user_choice > computer_choice:
      print("Too High!")
      lives -= 1
      print(f"You have {lives} lives left")
      if lives == 0:
        print("Game Over, U lost :C")
        break
    elif user_choice < computer_choice:
      print("Too Low!")
      lives -= 1
      if lives == 0:
        print("Game Over, U lost :C")
        break
      print(f"You have {lives} lives left")
  user_choice2 = input("Do u want to play again? (y/n): ")
  if user_choice2 == 'y' or user_choice2 == 'yes':
    system("CLS")
    run()
  else:
    print("Okay, Bye then!")
    exit()

run()