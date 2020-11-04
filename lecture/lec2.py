
def identity(k):
    return k

def cube(k):
    return k*k*k

def summation(n,term):
    '''sum the first terms

    >>> summation(5, cube)
    225
    '''
    total,k=0,1
    while k<=n:
        total,k=total+ term(k) ,k+1
    return total




def sum_naturals(n):
    '''sum the first n numbers

    >>> sum_naturals(5)
    15
    '''
    return summation(n, identity)

def sum_cubes(n):
    '''sum the first

    >>> sum_cubes(5)
    225
    '''
    return summation(n,cube)
