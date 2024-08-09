import random

random_number = random.randint(1,100)

guess = int(input("Enter your guess: "))

while True:
    if guess > random_number:
        print("Too high!")
        guess = int(input("Enter your guess:"))
    elif guess < random_number:
        print("Too low!")
        guess = int(input("Enter your guess:"))
    else:
        print("You won!")
        break





