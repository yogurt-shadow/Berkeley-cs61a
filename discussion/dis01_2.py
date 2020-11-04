#2.1
def keep_ints(cond, n):
    '''Print out all integers 1..i..n where cond(i) is true

    >>> def is_even(x):
    ...     return x % 2 ==0
    >>> keep_ints(is_even, 5)
    2
    4
    '''

    '''Here is My Code'''
    k = 1
    while k <= n:
        if cond(k):
            print(k)
            k=k+1
        else:
            k=k+1
        '''AC'''

#2.2 is a WWPD

#2.3
def keep_ints2(n):
    '''returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns true

    >>> def is_even(x):
    ...     return x % 2 ==0
    >>> keep_ints2(5)(is_even)
    2
    4
    '''

    '''Here is My Code'''
    def f(x):
        k=1
        while k<=n:
            if x(k):
                print(k)
                k=k+1
            else:
                k=k+1
    return f
    '''AC'''
    
