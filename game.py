import random


input_name = input("Whats your name\n")


def greeting():
    print(
        f"{input_name}, i'm thinking of a number between 1 and 100\nTry to guess my number"
    )


greeting()


def guess():
    number = random.randint(1, 100)
    print(number)
    guess = 0
    i = 0
    while guess != number:
        i += 1
        guess = int(input("Your guess? "))
        print(guess)
        if guess == number:
            break

    print(f"finished in {i} tries")


guess()
