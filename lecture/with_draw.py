def percent_difference(x, y):
    difference = abs(x - y)
    return 100 * difference / x

def make_withdraw(balance):
    '''return a withdraw function with a starting balance.'''
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "aaa"
        balance = balance - amount
        return balance
    return withdraw
