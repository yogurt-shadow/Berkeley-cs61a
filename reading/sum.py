def sum_naturals(n):
    '''return the sum of first n integers.

    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    '''
    total,k=0,1
    while k<=n:
        total,k=total+k,k+1
    return total
