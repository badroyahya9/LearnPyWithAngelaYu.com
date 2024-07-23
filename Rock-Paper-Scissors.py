
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

rock_paper_scissors = [rock, paper, scissors]
print("Welcome to rock-paper-scissors game!!")
user_choice = int(input("What do you choose ? 0 for Rock , 1 for Paper and 2 for Scissors :\n"))
paint = rock_paper_scissors[user_choice]
print(paint)

pc_choice = random.randint(0, 2)
paint2 = rock_paper_scissors[pc_choice]


if user_choice == 0 and pc_choice == 2:
    print("Computer choose :\n")
    print(paint2)
    print("You won!!")
if user_choice == 0 and pc_choice == 0:
    print("Computer choose :\n")
    print(paint2)
    print("draw")
if user_choice == 0 and pc_choice == 1:
    print("Computer choose :\n")
    print(paint2)
    print("You lost!!")
if user_choice == 1 and pc_choice == 0:
    print("Computer choose :\n")
    print(paint2)
    print("You won!!")
if user_choice == 1 and pc_choice == 1:
    print("Computer choose :\n")
    print(paint2)
    print("draw")
if user_choice == 1 and pc_choice == 2:
    print("Computer choose :\n")
    print(paint2)
    print("You lost!!")
if user_choice == 2 and pc_choice == 1:
    print("Computer choose :\n")
    print(paint2)
    print("You won!!")
if user_choice == 2 and pc_choice == 2:
    print("Computer choose :\n")
    print(paint2)
    print("draw")
if user_choice == 2 and pc_choice == 0:
    print("Computer choose :\n")
    print(paint2)
    print("You lost!!")



