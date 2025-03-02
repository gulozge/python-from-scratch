import random


def play():
    user = input(
        "What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "It\'s a tie"

    if is_win(user, computer):
        return "you won!"
    else:
        return "you lost"

# r > s, s > p, p > r


def is_win(user, computer):
    if (user == "r" and computer == "s") or (user == "s" and computer == "p") or (user == "p" and computer == "r"):
        return True
    return False


print(play())
