def count(s, value):
    '''Count the number of times that value appears
    in sequence s

    >>> count([1, 2, 1, 2, 1], 1)
    3
    '''
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total

def cheer():
    for _ in range(3):
        print('Go Bears!')
