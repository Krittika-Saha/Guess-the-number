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
  1. I'll be guessing a number from 1-100
  2. You have to guess it
  3. Enjoy! 
    """)
  lives = select_mode(input("What mode do you want to play the game in?").lower())
  computer_choice = select_random(number_list)
  print("""
  Okay, I'm thinking of a number
  """)
  print(f"Psst, the number is {computer_choice}")
  while True:
    user_choice = int(input("Guess my number: "))
    if user_choice == computer_choice:
      print("Good Job! U won!")
      break
    elif user_choice > computer_choice:
      print("Too High!")
      lives -= 1
      print(f"You have {lives} lives left")
    elif user_choice < computer_choice:
      print("Too Low!")
      lives -= 1
      print(f"You have {lives} lives left")
    elif lives == 0:
      print("Game Over, U lost :C")
      break
  user_choice2 = input("Do u want to play again? (y/n): ")
  if user_choice2 == 'y' or user_choice2 == 'yes':
    system("CLS")
    run()
  else:
    print("Okay, Bye then!")
    exit()

run()