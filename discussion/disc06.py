class Link:
    empty=()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


def multiply_lnks(lst_of_lnks):
    '''
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest
    ()
    '''
    if Link.empty in (lst_of_lnks):
        return Link.empty
    else:
        lst = lst_of_lnks
        result = Link(1)
        first_ele =[ele.first for ele in lst]
        first = 1
        for i in first_ele:
            first = first * i
        result.first = first
        result.rest = multiply_lnks([ele.rest for ele in lst])
        return result

def remove_duplicates(lnk):
    '''
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> unique = remove_duplicates(lnk)
    >>> unique
    Link(1, Link(5))
    >>> lnk
    Link(1, Link(5))
    '''
    if lnk.rest is Link.empty:
        return lnk
    elif lnk.second == lnk.first:
        lnk.rest = lnk.rest.rest
        lnk = remove_duplicates(lnk)
    else:
        lnk.rest = remove_duplicates(lnk.rest)
    return lnk


def even_weighted(lst):
    '''
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    '''
    return [ele * lst.index(ele) for ele in lst if lst.index(ele) % 2 == 0]

def quicksort_list(lst):
    '''
    >>> quicksort_list([3, 1, 4])
    [1, 3, 4]
    '''
    if not lst:
        return []
    pivot = lst[0]
    less = [ele for ele in lst if ele < pivot]
    greater = [ele for ele in lst if ele > pivot]
    return quicksort_list(less) + [pivot] + quicksort_list(greater)

def max_product(lst):
    '''
    >>> max_product([10, 3, 1, 9,2])
    90
    >>> max_product([5, 10, 5, 10, 5])
    125
    >>> max_product([])
    1
    '''
    if not lst:
        return 1
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return max(lst)
    if len(lst) == 3:
        return max(lst[0]*lst[2], lst[1])
    else:
        return max(lst[0] * max_product(lst[2:]), lst[1] * max_product(lst[3:]))
