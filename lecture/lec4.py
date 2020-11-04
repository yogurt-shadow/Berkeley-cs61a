#compute Fibonacci by difference

def fib(x):
    '''
    >>> fib(0)
    0
    >>> fib(8)
    21
    >>> fib(12)
    144
    '''
    if not x:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-2)+fib(x-1)

def end(n,d):
    '''print the final digits of N in reverse order until d is found

    >>> end(34567,5)
    7
    6
    5
    '''
    while  n:
        digit = n % 10
        print(digit)
        if digit == d:
            return
        n = n // 10
    return

def h(f):
    def g(*args):
        print(*args)
        return
    return g
