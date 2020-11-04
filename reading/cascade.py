def cascade(n):
    '''
    >>> cascade(2017)
    2017
    201
    20
    2
    20
    201
    2017
    '''
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)
