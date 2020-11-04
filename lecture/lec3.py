

def make_adder(n):
    '''return a function that take s one
    K and return K + N

    >>> add_three = make_adder(3) #  add _three is actually a function
    >>> add_three(4)
    7
    '''
    def adder(k):
        return k+n
    return adder
