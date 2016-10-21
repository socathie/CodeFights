def tennisSet(score1, score2):
    if score1 < score2:
        tmp =  score1
        score1 = score2
        score2 = tmp
    if score1 == 6 and score2 < 5 or score1 == 7 and score2 < 7 and score2 >= 5:
        return True
    return False
