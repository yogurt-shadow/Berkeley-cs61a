def is_even(n):
    '''
    >>> is_even(7)
    False
    >>> is_even(12)
    True
    '''
    if n == 0:
        return True
    else:
        return is_odd(n-1)

def is_odd(n):
    '''
    >>> is_odd(13)
    True
    >>> is_odd(100)
    False
    '''
    if n == 0:
        return False
    else:
        return is_even(n-1)
