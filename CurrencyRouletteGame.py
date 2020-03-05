import requests
import random


def get_money_interval(difficulty):
    r = requests.get('https://api.exchangeratesapi.io/latest?base=USD&symbols=USD,ILS')
    dict_r = r.json()
    new_r = round(dict_r['rates']['ILS'],2)
    gen = random.randrange(1,100)
    t = new_r * gen
    print("Dollar amount is {}.".format(gen))

    interval = (t - (5-difficulty)),(t + (5-difficulty))
    return interval


def get_guess_from_user():
    prompt = int(input("What do you think is the Value in ILS ? "))
    return prompt


def play(difficulty):
    interval = get_money_interval(difficulty)
    prompt = get_guess_from_user()
    if prompt >= interval[0] <= interval[1]:
        print("YOU WON")
    else:
        user = input("You lose, Try again ? [yes/no] ")
        if user == "yes" or user == "y":
            play(difficulty)
