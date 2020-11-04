def print_all(x):
    print(x)
    return print_all

def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x+y)
    return next_sum
