import GuessGame
import MemoryGame
import CurrencyRouletteGame


def welcome(name):
    print("\nHello " + name + " and welcome to the World of Games (WoG).")
    print("Here you can find many cool games to play.")


def load_game():

    should_continue = True

    while should_continue:
        print("\nPlease choose a game to play: ")
        print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
        print("2. Guess Game - guess a number and see if you chose like the computer")
        print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
        game = input("Please choose a game to play: ")
        while game not in ['1','2','3']:
            game = input("\nWrong choice please try again. Please choose 1-3.\n")

        while True:
            difficulty = input("Please choose game difficulty from 1 to 5: ")
            if difficulty in ['1','2','3','4','5']:
                break
            else:
                print("\nWrong choice please try again\n")

        if game == "1":
            MemoryGame.play(int(difficulty))
        elif game == "2":
            GuessGame.play(int(difficulty))
        elif game == "3":
            CurrencyRouletteGame.play(int(difficulty))
        should_continue = get_should_continue()


def get_should_continue():
    got_valid_input = False
    while not got_valid_input:
        print("\nReturn to Main menu ? [yes/no] ")
        user = input("")
        if user == "yes" or user == "y":
            return True
        elif user == "no" or user == "n":
            print("\nThank you for playing")
            return False
