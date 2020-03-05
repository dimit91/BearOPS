import random
import time


def generate_sequence(difficulty):
    lst = []
    for i in range(1,difficulty+1):
        rand_num = random.randint(1,101)
        lst.append(str(rand_num))
        print(lst)
        time.sleep(0.7)
    from Utils import screen_cleaner
    screen_cleaner()
    return lst


def get_list_from_user(difficulty):
    print("Try to guess the numbers you've just saw")
    lst = []
    for i in range(1, difficulty+1):
        user_input = str(input())
        lst.append(user_input)
    return lst


def is_list_equal(x, y):
    if x == y:
        return True
    else:
        return False


def play(difficulty):
    gen_list = generate_sequence(difficulty)
    guess_list = get_list_from_user(difficulty)
    compare = is_list_equal(gen_list,guess_list)

    while compare == False:
        user = input("You lose, Try again ? [yes/no] ")
        if user == "yes" or user == "y":
            play(difficulty)
            break

        elif user == "no" or user == "n":
            return True
    if compare == True:
        print("You Won")
