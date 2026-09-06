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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = (rock, paper, scissors)

choose = int(input("Choose 0 for rock, 1 for paper, or 2 for scissors:\n"))

if choose < 0 or choose > 2:
    print("Please choose a valid number.")

else:
    print("You chose:")
    print(options[choose])

    if choose == 0:
        print("Rock\n")
    elif choose == 1:
        print("Paper\n")
    elif choose == 2:
        print("Scissors\n")

    computer_choice = random.randint(0, 2)

    print("Computer chose:")
    print(options[computer_choice])

    if computer_choice == 0:
        print("Rock\n")
    elif computer_choice == 1:
        print("Paper\n")
    elif computer_choice == 2:
        print("Scissors\n")

    if (
        computer_choice == 0 and choose == 1
        or computer_choice == 1 and choose == 2
        or computer_choice == 2 and choose == 0
    ):
        print("You Won!")

    elif computer_choice == choose:
        print("It's a draw.")

    else:
        print("You Lose.")