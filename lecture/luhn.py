def split(n):
    return n//10 , n%10

def sum_digits(n):
    if n< 10:
        return n
    else:
        all_bust_last, last =split(n)
        return sum_digits(all_bust_last) + last


def luhn(n):
    kk , total = 1, 0
    while n:
        digit = n % 10
        if kk % 2 == 1:
            total = total + digit
        else:
            total = total + sum_digits(2*digit)
        kk = kk + 1
        n = n // 10
    return total

def luhn_sum(n):
    if n< 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last)+ last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2*last)
    if n<10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

'''about the main idea:
    the number goes into luhn_sum and split to two parts
    the all_but_last goes into luhn_sum_double
    and notice that the last number doubles two
    then split and goes back to the luhn_sum

    the main point is that each second number is operated
    in luhn_sum_double and each odd number is operated
    in luhn_sum
'''
