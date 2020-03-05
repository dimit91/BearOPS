def add_score(difficulty):
    try:
        points_of_winning = (int(difficulty) * 3) + 5
        from Utils import SCORES_FILE_NAME
        # scores = SCORES_FILE_NAME
        open_scores = open("Scores.txt", "r")
        read_scores = open_scores.read()

        read_scores = int(read_scores) + int(points_of_winning)
        open_scores.close()

        open_scores = open("Scores.txt", "w")
        open_scores.write(str(read_scores))
        open_scores.close()

    except:
        # print("Error")
        file_open = open("Scores.txt", "w")
        file_open.write(str(difficulty))
        file_open.close()


