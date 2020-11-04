#constructor
def tree(label, branches = []):
    return [label] + list(branches)

#selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

#for convenience
def is_leaf(tree):
    return not branches(tree)

#3.1
def tree_max(t):
    return max([label(t)] + [tree_max(branch) for branch in branches(t)])

def height(t):
    if is_leaf(t):
        return 1
    else:
        return 1 + max([height(branch) for branch in branches(t)])

def square_tree(t):
    if is_leaf(t):
        return tree(label(t) * label(t))
    else:
        return tree(label(t) * label(t), [square_tree(branch) for branch in branches(t)])


def find_path(tree, x):
    '''
    >>> t = tree(2,[tree(7,[tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)
    '''
    def in_tree(tree1, x1):
        if label(tree1) == x1:
            return True
        else:
            list = [in_tree(branch, x1) for branch in branches(tree1)]
            return True in list
    if not in_tree(tree, x):
        return None
    elif label(tree) == x:
        return [x]
    else:
        for branch in branches(tree):
            if in_tree(branch, x):
                return [label(tree)] + find_path(branch, x)

def prune(t,k):
    if k == 1:
        return tree(label(t))
    else:
        
        return tree(label(t),[prune(branch, k - 1) for branch in branches(t)] )
