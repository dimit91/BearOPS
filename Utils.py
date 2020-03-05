SCORES_FILE_NAME = open("Scores.txt", "a")
BAD_RETURN_CODE = str(99999)


def screen_cleaner():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
