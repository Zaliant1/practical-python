import random

choices = ['scissors', 'rock', 'paper']

computer_choice = random.choice(choices)


user_choice = input('Do you want - rock, paper, or scissors?\n')

if computer_choice == user_choice:
    print(f'computer played {computer_choice}, TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print(f'computer played {computer_choice}, WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print(f'computer played {computer_choice}, WIN')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print(f'computer played {computer_choice}, WIN')
else:
    print(f'computer played {computer_choice}, LOSE')
