def tree(label, branches=[]):
    return [label] + list(branches)

def label(trees):
    return trees[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def sum_range(t):
    def helper(t):
        if is_leaf(t):
            return [label(t), label(t)]
        else:
            a = min([helper(branch)[1] for branch in branches(t)])
            b = max([helper(branch)[0] for branch in branches(t)])
            x = label(t)
            return [b + x, a + x]
    x, y = helper(t)
    return x - y

def no_eleven(n):
    if n == 0:
        return [[]]
    elif n == 1:
        return [[6], [1]]
    else:
        a, b = no_eleven(n - 1), no_eleven(n - 2)
        return [ s + [6]  for s in a] + [ s + [6, 1]  for s in b]

def eval_with_add(t):
    '''
    >>> plus = tree('+', [tree(2), tree(3)])
    >>> eval_with_add(plus)
    5
    >>> times = tree('*', [tree(2), tree(3)])
    >>> eval_with_add(times)
    6
    >>> deep = tree('*', [tree(2), plus, times])
    >>> eval_with_add(deep)
    60
    >>> eval_with_add(tree('*'))
    1
    '''
    if label(t) == '+':
        return sum([eval_with_add(branch) for branch in branches(t)])
    elif label(t) == '*':
        total = 1
        for b in branches(t):
            total, term = 0, total * eval_with_add(b)
            for i in range(1):
                total = total + term
        return total
    else:
        return label(t)
