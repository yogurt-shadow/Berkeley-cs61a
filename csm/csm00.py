def mystery(f,x):
    '''
    >>> from operator import add, mul
    >>> a = mystery(add, 3)
    >>> a(4)   # add(3,4)
    7
    >>> a(12)
    15
    >>> b = mystery(mul, 5)
    >>> b(7)  # mul(5,7)
    35
    >>> b(1)
    5
    >>> c = mystery(lambda x, y: x * x + y, 4)
    >>> c(5)
    21
    >>> c(7)
    23
    '''
    return lambda y: f(x, y)

def fox_says(start, middle, end, num):
    '''
    >>> fox_says('wa', 'pa', 'pow', 3)
    'wa-pa-pa-pa-pow'
    >>> fox_says('fraka', 'kaka', 'kow', 4)
    'fraka-kaka-kaka-kaka-kaka-kow'
    '''
    def repeat(k):
        if k == 1:
            return middle
        else:
            return repeat(k - 1) + '-' + middle
    return start +'-'+repeat(num) + '-' + end

from operator import mul, add, pow
def combine(n, f, result):
    '''
    combine the digits in non_negative integer n using f.

    >>> combine(3, mul, 2)  #mul(3,2)
    6
    >>> combine(43, mul, 2)
    24
    >>> combine(6502, add, 3)
    16
    >>> combine(239, pow, 0)
    8
    '''
    if n == 0:
        return result
    else:
        return combine(n // 10, f, f(n % 10, result))

def has_sum(total, n, m):
    '''
    >>> has_sum(1, 3, 5)
    False
    >>> has_sum(5, 3, 5)   # 0*3 + 1*5 = 5
    True
    >>> has_sum(11, 3, 5)  # 2*3 + 1*5 = 11
    True
    >>> has_sum(23, 3, 5)
    True
    '''
    if total % n == 0 or total % m == 0:
        return True
    elif total > n and total > m:
        return has_sum(total - n, n, m)
    else:
        return False

def sum_range(lower, upper):
    '''
    >>> sum_range(45, 60)   # printer 1 prints within this range
    True
    >>> sum_range(40, 55)   # printer 1 can print a number 56 - 60
    False
    >>> sum_range(170, 201) # printer 1 + 2 will print between 180 and 200 copies total
    True
    '''
    def copies(pmin, pmax):
        if lower <= pmin and upper >= pmax:
            return True
        elif upper < pmin:
            return False
        return copies(pmin + 50, pmax + 60) or copies(pmin + 130, pmax + 140)
    return copies(0, 0)
