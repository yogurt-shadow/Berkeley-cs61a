def list_of_lists(lst):
    '''
    >>> list_of_lists([1,2,3])
    [[0], [0, 1], [0, 1, 2]]

    >>> list_of_lists([1])
    [[0]]
    >>> list_of_lists([])
    []
    '''
    if not lst:
        return []
    else:
        return [list(range(n)) for n in lst]

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


t = tree(9,[tree(2), tree(4,[tree(1)]), tree(4,[tree(7), tree(3)])])
def sum_of_nodes(t):
    if not branches(t):
        return label(t)
    else:
        sum_branches = [sum_of_nodes(branch) for branch in branches(t)]
        return label(t) + sum(sum_branches)
