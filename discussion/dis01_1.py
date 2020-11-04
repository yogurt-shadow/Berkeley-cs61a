#1.1
def wears_jacket(temp,raining):
    '''
    >>> wears_jacket(90,False)
    False
    >>> wears_jacket(40,False)
    True
    >>> wears_jacket(100,True)
    True
    '''

    '''Here is My Code'''
    return (temp<60) or raining
    '''AC'''

#1.2
def handle_overflow(s1, s2):
    '''
    >>> handle_overflow(27, 15)
    No overflow
    >>> handle_overflow(35, 29)
    Move to Section 2: 1
    >>> handle_overflow(20, 32)
    Move to Section 1: 10
    >>> handle_overflow(35, 30)
    No space left in either section
    '''

    '''Here is My Code'''
    if s1 < 30 and s2 < 30:
        print('No overflow')
    elif s1 >= 30 and s2 < 30:
        print('Move to Section 2:',30-s2)
    elif s1 < 30 and s2 >= 30:
        print('Move to0</60>+0                                Section 1:',30-s1)
    else:
        print('No space left in either section')
        '''AC'''

#1.3
def square(x):
    return x*x

def so_slow(num):
    x = num
    while x > 0:
        x=x+1
    return x / 0
    '''
    so_slow(5) is a infinite loop
    don't get in the trap
    '''

#1.4
def is_prime(n):
    '''
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    '''

    '''Here is My Code'''
    num = 2
    while num <= n //2:
        if n % num ==0:
            return False
        num = num + 1
    return True
