import random
def score(p, count):
    '''
    return score_got, count of wins
    '''
    a = random.random()
    if a >= p:     #lose the game
        return -1, 0
    elif count < 2:
        return 1, count + 1
    else:
        return 2, count + 1
