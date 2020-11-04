def longest_increasing_suffix(n):
    '''return the longest increasing suffix of a positive interger n.

    >>> longest_increasing_suffix(63134)
    134
    >>> longest_increasing_suffix(233)
    3
    >>> longest_increasing_suffix(5689)
    5689
    >>> longest_increasing_suffix(568901)
    1
    '''

    m, suffix, k = 10, 0 , 1

    while n:
        n, last = n // 10, n % 10
        if last * (k //10) < suffix or suffix == 0:
            m, suffix, k = 10, last * k + suffix , 10 * k
        else:
            return suffix
    return suffix
    '''
    God Damn that m!!!!!!
    '''

def sandwich(n):
    '''return true if n contains a sandwich and false otherwise

    >>> sandwich(416263)   #626
    True
    >>> sandwich(5050)     #505 or 050
    True
    >>> sandwich(4441)     #444
    True
    >>> sandwich(1231)
    False
    >>> sandwich(55)
    False
    >>> sandwich(4456)
    False
    '''

    tens, ones = n // 10 % 10, n % 10
    n = n // 100
    while n:
        if n % 10 == ones or n //10 % 10 == tens:
            return True
        else:
            tens, ones = n // 10 % 10, n % 10
            n = n // 100
    return False

def luhn_sum(n):
    '''return the luhn sum of n.

    >>> luhn_sum(135)    # 1+6+5
    12
    >>> luhn_sum(185)    #1+(1+6)+5
    13
    >>> luhn_sum(138743) # 2+3+(1+6)+7+8+3
    30
    '''
    def luhn_digit(digit):
        x = digit * (multiplier + 1) // 2 + digit * 2 * (multiplier - 1) // (-2)
        return (x // 10) + (x % 10)
    total, multiplier = 0, 1
    while n:
        n, last = n // 10, n % 10
        total = total + luhn_digit(last)
        multiplier = 0 - multiplier

    return total
    '''
    Hint: attention that multiplier can be used in the function of luhn_digit
    and the expression should consider both two circumstances (single and double)
    '''

def square(x):
    return lambda x: x*x
def dog(bird):
    def cow(tweet, moo):
        woof = bird(tweet)
        print(moo)
        return woof
    return cow
