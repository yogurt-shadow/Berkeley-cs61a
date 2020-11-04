class Account:
    '''
    >>> a = Account('John')
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds'
    >>> a.balance
    10
    '''
    interest = 0.02
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            return 'Insufficient funds'
        else:
            self.balance = self.balance - amount
            return self.balance
