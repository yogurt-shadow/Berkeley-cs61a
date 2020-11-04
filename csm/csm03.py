def accumulate(lst):
    '''
    >>> l = [1, 5, 13, 4]
    >>> accumulate(l)
    23
    >>> l
    [1, 6, 19, 23]
    >>> deep_l = [3, 7, [2, 5, 6], 9]
    >>> accumulate(deep_l)
    32
    >>> deep_l
    [3, 10, [2, 7, 13], 32]
    '''
    total , sum_list = 0, []
    for ele in lst:

        if isinstance(ele, list):
            inside = accumulate(ele)
            total = total + inside
            sum_list.append(ele)
        else:
            total = total + ele
            sum_list.append(total)
    for i in range(len(lst) - 1):
        lst.pop()
    lst.pop()
    for i in range(len(sum_list) - 1):
        lst.append( sum_list[i])
    lst.append(sum_list[-1])
    return total


def has_seven(k):
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def make_pingpong_tracker():
    '''
    >>> output = []
    >>> x = make_pingpong_tracker()
    >>> for _ in range(9):
    ...     output += [x()]
    >>> output
    [1, 2, 3, 4, 5, 6, 7, 6, 5]
    '''
    index, current, add = 1, 0, True
    def pingpong_tracker():
        nonlocal current, index, add
        if add:
            current = current + 1
        else:
            current = current - 1
        if has_seven(index) or index % 7 == 0:
            add = not add
        index = index + 1
        return current
    return pingpong_tracker
