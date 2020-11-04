def search(f):
    x = 0
    while True:
        if f(x):
            return x
        else:
            x = x + 1


def is_three(x):
    return x == 3

def square(x):
    return x*x

def positive(x):
    return max(0,square(x) - 100)

def inverse(f):
    '''return the inverse of function f'''
    return lambda y: search(lambda x: f(x) == y)
    '''
    Self Explanation Here
    note that search(lambda x : f(x) == y) returns a value of x which makes
    that f(x) == y is true.
    Then the lambda y: x returns a function(actually what we want to find) that
    makes input value y changes to output value x.
    So the equation f(x)=y and g(y)=x makes sense.
    And that function g is exactly what we need.
    '''
