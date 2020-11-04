def product(n,m):
    if m == 1:
        return n
    else:
        return n + product(n, m - 1)

def countdown(n):
    '''
    >>> countdown(3)
    3
    2
    1
    '''
    if n == 1:
        print("1")
    else:
        print(n)
        countdown(n - 1)

def countup(n):
    '''
    >>> countup(5)
    1
    2
    3
    4
    5
    '''
    if n == 1:
        print("1")
    else:
        countup(n - 1)
        print(n)

def sum_digits(n):
    '''
    >>> sum_digits(7)
    7
    >>> sum_digits(30)
    3
    >>> sum_digits(228)
    12
    '''
    if n < 10:
        return n
    else:
        return n % 10 +sum_digits(n // 10)

def count_stair_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def count_k(n, k): #DIFFICULT
    '''
    >>> count_k(3,3) #3, 2+1, 1+2, 1+1+1
    4
    >>>
    count_k(4,4)
    8
    >>> count_k(10,3)
    274
    >>> count_k(300,1)
    1
    '''
    #noting: different from reading
    '''
    Hint
    count_k(n,k) = count_k(n - 1, k) + count_k(n - 2, k)+ ... +count_k(n -k, k)
    '''
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        total, i = 0, 1
        while i <= k:
            total = total + count_k(n - i, k)
            i = i + 1
        return total
