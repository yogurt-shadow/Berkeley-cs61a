def gcd(m, n):
    '''return the largest k that divides both m and n
    k, m, n are all posotive integers
    >>> gcd(12,8)
    4
    >>> gcd(16,12)
    4
    >>> gcd(16,8)
    8
    >>> gcd(2,16)
    2
    >>> gcd(5,5)
    5
    '''
    if m == n:
        return m
    else:
        return gcd(abs(m-n), min(m, n))

def add_all(n):
    print(n)
    def next_add(m):
        return add_all(n+m)
    return next_add

curry2 =lambda f: lambda x: lambda y: f(x, y)

square = lambda x: x*x
def sum_squares_up_to(n):
    if n == 1:
        return 1
    else:
        return square(n) +sum_squares_up_to(n-1)
