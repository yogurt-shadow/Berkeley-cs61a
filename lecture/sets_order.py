class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)


def filter_link(f, s):
    '''return ele of s where f(ele) is true.'''
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered

def extend_link(s, t):
    if empty(s):
        return t
    else:
        return Link(s.first, extend_link(s.rest , t))


def empty(s):
    return s is Link.empty

def contains(s, v):
    '''
    >>> s =Link(1, Link(3, Link(2)))
    >>> contains(s, 2)
    True
    >>> contains(s, 5)
    False
    '''

    if empty(s):
        return False
    elif s.first == v:
        return True
    else:
        return contains(s.rest, v)


def intersect(set1, set2):
    if empty(set1) or empty(set2):
        return Link.empty
    if set1.first == set2.first:
        return Link(set1.first, intersect(set1.rest, set2.rest))
    elif set1.first > set2.first:
        return intersect(set1, set2.rest)
    else:
        return intersect(set2, set1.rest)

def union(set1, set2):
    if empty(set1):
        return set2
    elif empty(set2):
        return set1
    else:
        if set1.first == set2.first:
            return Link(set1.first, union(set1.rest, set2.rest))
        elif set1.first > set2.first:
            return Link(set2.first, union(set1, set2.rest))
        else:
            return Link(set1.first, union(set2, set1.rest))

def add_list(s, v):
    assert not empty(s), "Cannot add to an empty set."
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and empty(s.rest):
        s.rest = Link(v, s.rest)
    elif s.first < v:
        s.rest = add_list(s.rest, v)
    return s
