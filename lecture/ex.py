'''
our first file

'''

from operator import floordiv,mod
def divide_exact(n,d):

    return floordiv(n,d),mod(n,d)

def absolute(x):

    if x<0:
        return -x
    elif x==0:
        return 0
    else:
        return x
    
