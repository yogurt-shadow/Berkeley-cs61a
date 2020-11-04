
def split(n):
    return n // 10, n % 10
def split_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return last + split_sum(all_but_last)


def luhn(x):
    all_but_last, last = split(x)
    return last + luhn_double(all_but_last)

def luhn_double(x):
    if x <10:
        return split_sum(2*x)
    else:
        all_but_last, last = split(x)
        return split_sum(2 * last) +luhn(all_but_last)
