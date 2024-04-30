import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")

difficulty = input("Chose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempts = 10

else:
    attempts = 5

number = random.choice(range(1, 100))

def game(chances):
    if chances == 5:
        print("You have 5 attempts remaining to guess the number.")
    elif chances == 10:
        print("You have 10 attempts remaining to guess the number.")

    while chances >= 0:
        guess = int(input("Make a guess: "))
        
        if chances == 0:
            print("You're no of attempts to guess the number have been completed, You lost!")
            break

        elif guess > number:
            print("Too high")
            chances -= 1

        elif guess < number:
            print("Too low")
            chances -= 1

        elif guess == number:
            print(f"You've got it, the answer was {number}")
            break

game(chances=attempts)

