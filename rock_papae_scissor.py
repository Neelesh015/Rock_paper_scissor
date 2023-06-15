import random

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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = print(input('''What do you want to choose?"
      type 0 for rock ,
      type 1 for paper,
      type 2 for scissor.\n'''))

game = ["rock", "paper", "scissor"]

computer = random.choice(game)
print(computer)

if paper == rock:
    print("user wins")
elif rock == scissor:
    print("user wins")
elif scissor == paper:
    print("user wins")
else:
    print("computer wins")
