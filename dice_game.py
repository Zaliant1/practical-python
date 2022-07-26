import random


def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total


def main():
    player1 = input("Enter player1 name: ")
    player2 = input("Enter player2 name: ")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(f"{player1} rolled {roll1}")
    print(f"{player2} rolled {roll2}")

    if roll1 > roll2:
        print(f"{player1} wins")
    elif roll2 > roll1:
        print(f"{player2} wins")
    else:
        print("tie")


main()
