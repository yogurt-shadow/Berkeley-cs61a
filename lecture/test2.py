class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    4
    >>> start.next().next().next().next().next()
    7
    >>> start.next().next().next().next().next().next()
    13
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    13
    """

    def __init__(self, value=0):
        self.value = value


    def next(self):
        "*** YOUR CODE HERE ***"
        if not self.value:
            result = Fib(1)
        elif self.value == 1 and self.prev == 0:
            result = Fib(1)
            result.prev2 = 0
        else:
            result = Fib(self.value + self.prev + self.prev2)
            result.prev2 = self.prev
        result.prev = self.value
        return result



    def __repr__(self):
        return str(self.value)
