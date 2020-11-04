def score(p, count):
    '''
    return score_got, count of wins
    '''
    import random
    a = random.random()
    if a >= p:     #lose the game
        return -1, 0
    elif count < 2:
        return 1, count + 1
    else:
        return 2, count + 1

def number(start, end, p, count):
    current, num = start, 0
    while current < end:
        gain , count = score(p, count)
        num = num + 1
        if current > start or gain > 0:
            if gain > 0 or (current + gain) % 15 != 0:
                current = current + gain
    return num

def get_list(chance, start, end, p, count):
    pro = []
    for i in range(chance):
        pro = pro + [number(start, end, p, count)]
    return pro

def makeup(list):
    result = []
    while list:
        a = min(list)
        fre = 0
        for i in list:
            if i == a:
                fre = fre + 1
        list = [j for j in list if j != a]
        result = result + [a] + [fre]
    return result

def expect(list):
    total, times = 0, 0
    for i in range(len(list)):
        if i % 2 == 0:
            product1 = list[i]
        else:
            total = product1 * list [i] + total
            times = times + list[i]
    return total / times

def final(chance, start, end, p, count):
    list = get_list(chance, start, end, p, count)
    list = makeup(list)
    return expect(list)
