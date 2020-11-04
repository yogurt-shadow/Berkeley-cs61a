def memory(n):
    '''
    >>> f = memory(10)
    >>> f(lambda x: x*2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    '''
    def h(func):
        nonlocal n
        n =  func(n)
        return n
    return h

def add_this_many(x, el, lst):
    '''
    >>> lst = [1,2,4,2,1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    '''
    num = lst.count(x)
    for i in range(num):
        lst.append(el)

def reverse(lst):
    '''
    >>> x =[3, 2, 4, 5, 1]
    >>> reverse(x)
    >>> x
    [1, 5, 4, 2, 3]
    '''
    x =[]
    while lst:
        ele = lst.pop()
        x.append(ele)
    for ele in x:
        lst.append(ele)

def group_by(s, fn):
    '''
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x*x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    '''
    dic = {}
    for ele in s:
        num = fn(ele)
        if num not in dic:
            dic[num] = [ele]
        else:
            dic[num].append(ele)
    return dic

def replace_all_deep(d, x, y):
    '''
    >>> d={1: {2: 'x', 'x': 4}, 2: {4: 4, 5: 'x'}}
    >>> replace_all_deep(d, 'x', 'y')
    >>> d
    {1: {2: 'y', 'x': 4}, 2: {4: 4, 5: 'y'}}
    '''
    for ele in d.values():
        for ele2 in ele:
            if ele[ele2] == x:
                ele[ele2] = y
