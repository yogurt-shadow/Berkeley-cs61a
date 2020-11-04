def end(n,d):
    '''print the final digits of N in reverse order until D is found.

    >>> end(34567,5)
    7
    6
    5
    '''
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if d == last:
            return None
