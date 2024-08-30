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

game = [rock, paper, scissors]
#     0     1      2
user = int(input("enter 0,1,2\n"))
computer = random.randint(0, 2)
print("you enter", user)
print("computer choose", computer)
print(game[user])
computer_choice = random.randint(0, 2)
print("Computer chose: ")
print(game[computer_choice])

if user > computer and computer != 0:
  print("you win")
elif user < computer and user != 0:
  print("you lose")
elif computer == user:
  print("draw")
elif computer == 0 and user == 2:
  print("you lose")
elif user == 0 and computer == 2:
  print("you win")
if user >= 3 or user < 0:
  print("invalid num")
