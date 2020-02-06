import random


def generate_number(difficulty):
    secret_number = random.randint(1,difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    guess = input("Choose a number between 1 and " + str(difficulty) + " ")
    return guess


def compare_results(x,y):
    if int(x) == int(y):
        return True
    else:
        return False


def play(difficulty):
    x = generate_number(difficulty)
    y = get_guess_from_user(difficulty)
    z = compare_results(x,y)

    while z == False:
        user = input("You lose, Try again ? [yes/no] ")
        if user == "yes" or user == "y":
            play(difficulty)
            break

        elif user == "no" or user == "n":
            return True
    if z == True:
        print("You Won")






