def make_withdraw(balance):
    '''return a withdraw function with a starting balance.'''
    def withdraw(amount):
        nonlocal balance
        balance = balance - amount
        return balance
    return withdraw
