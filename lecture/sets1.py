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

def adjoin(s, v):
    if contains(s, v):
        return s
    else:
        return Link(v, s)  # no order for sets

def intersect(set1, set2):
    in_set2 = lambda x: contains(set2, x)
    return filter_link(in_set2, set1)

def union(set1, set2):
    not_in_set2 = lambda x: not contains(set2, x)
    set1_not_set2 = filter_link(not_in_set2, set1)
    return adjoin(set1_not_set2, set2)
