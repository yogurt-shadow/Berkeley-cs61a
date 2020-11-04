class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.second
    3
    >>> s.first = 5
    >>> s.second = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value


    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


def skip(lst):
    '''
    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> a
    Link(1, Link(2, Link(3, Link(4))))
    >>> b = skip(a)
    >>> b
    Link(1, Link(3))
    >>> a
    Link(1, Link(2, Link(3, Link(4))))
    '''
    if lst.rest is Link.empty or lst.rest.rest is Link.empty:
        return Link(lst.first)
    else:
        s = Link(lst.first, skip(lst.rest.rest))
        return s


def skip2(lst):
    '''
    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> b = skip2(a)
    >>> b
    >>> a
    Link(1, Link(3))
    '''
    if lst.rest is Link.empty or lst.rest.rest is Link.empty:
        lst.rest = Link.empty
        return None
    else:
        lst.rest = skip(lst.rest.rest)
        return None

def reverse(lst):
    '''
    >>> a = Link(1, Link(2, Link(3)))
    >>> b = reverse(a)
    >>> b
    Link(3, Link(2, Link(1)))
    >>> a
    Link(1, Link(2, Link(3)))
    '''
    result = Link.empty
    while not lst is Link.empty:
        result = Link(lst.first , result)
        lst = lst.rest
    return result

class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = branches
    def is_leaf(self):
        return not self.branches

def contains_n(elem, n, t):
    '''
    >>> t1 = Tree(1, [Tree(1, [Tree(2)])])
    >>> contains_n(1, 2, t1)
    True
    >>> contains_n(2, 2, t1)
    False
    >>> contains_n(2, 1, t1)
    True
    >>> t2 = Tree(1, [Tree(2), Tree(1, [Tree(1), Tree(2)])])
    >>> contains_n(1, 3, t2)
    True
    >>> contains_n(2, 2, t2)
    False
    '''
    if n == 0:
        return True
    elif t.is_leaf():
        return t.label == elem and n <= 1
    elif t.label == elem:
        return True in [contains_n(elem, n-1, branch) for branch in t.branches]
    else:
        return True in [contains_n(elem, n, branch) for branch in t.branches]

def factor_tree(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return Tree(n, [Tree(i), factor_tree(n // i)])
    return Tree(n)
