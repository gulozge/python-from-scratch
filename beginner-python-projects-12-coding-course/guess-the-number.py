import random
# user


def guess(x: int):
    random_number = random.randint(1, x)
    while True:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
        else:
            print(
                f"Congratulations! You've guessed the number  {random_number}")
            break


# guess(5)
# -----------------------------------------------------------------------------------------------------------------------------------------
# computer
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while True:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        guess = random.randint(low, high)
        feedback = input(
            f"Is {guess} to low (L),to high(H),or correct (C)??").lower()
        if feedback == "h":
            high = guess-1
        elif feedback == "l":
            low = guess+1
        else:
            print(
                f"Congratulations! The computer  guessed your number {guess}")
            break


computer_guess(100)
