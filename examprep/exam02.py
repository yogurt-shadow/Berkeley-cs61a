def kbonacci(n, k):
    '''return element N of a K-bonacci sequence.

    >>> kbonacci(3, 4)
    1
    >>> kbonacci(9, 4)
    29
    >>> kbonacci(4, 2)
    3
    >>> kbonacci(8, 2)
    21
    '''
    if n < k - 1:
        return 0
    elif n == k - 1:
        return 1
    else:
        total = 0
        i = n - k
        while i < n:
            total = total + kbonacci(i, k)
            i = i + 1
        return total

def combine(left, right):
    '''return all of LEFT's digits followed by all of RIGHT's digits '''
    factor = 1
    while factor <= right:
        factor = factor * 10
    return left * factor + right

def reverse(n):
    '''return the digits of N in reverse.
    >>> reverse(122543)
    345221
    '''
    if n < 10:
        return n
    else:
        return combine(n % 10, reverse(n // 10))

def remove(n, digit):
    '''return all digits of N that are not DIGIT, for DIGIT less than 10.
    >>> remove(243132, 3)
    2412
    >>> remove(remove(243132, 1), 2)
    433
    '''
    removed = 0
    while n != 0:
        n, last = n // 10, n % 10
        if last != digit:
            removed = combine(removed, last)
    return reverse(removed)

square = lambda x: x*x
double = lambda x: 2*x
def memory(x, f):
    '''return a higher-order function that prints its memories.
    >>> f = memory(3, lambda x: x)
    >>> f = f(square)
    3
    >>> f = f(double)
    9
    >>> f = f(print)
    6
    >>> f = f(square)
    3
    None
    '''
    def g(h):
        print(f(x))
        return memory(x, h)
    return g

from operator import add
avengers = 6
def vision(avengers):
    print(avengers)
    return avengers + 1

def hawkeye(thor, hulk):
    love = lambda black_widow: add(black_widow, hulk)
    return thor(love)

def hammer(worthy, stone):
    if worthy(stone) < stone:
        return stone
    elif worthy(stone) > stone:
        return -stone
    return 0

capt = lambda iron_man: iron_man(avengers)
