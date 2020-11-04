def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def ensure_consistency(fn):
    n = 0
    z = {}
    def helper(x):
        nonlocal n
        n = n + 1
        if n > 20:
            return None
        val = fn(x)
        if x not in z:
            z[x] = [val]
        if z[x][0] == val:
            return val
        else:
            z[x] = None
            return z[x]
    return helper

def decrypt(s, d):
    '''
    >>> codes = {'alan': 'spooky', 'al':'drink', 'antu':'your','turing':'ghosts',
    ...  'tur':'scary','ing':'skeletons', 'ring':'ovaltine'}
    >>> decrypt('alanturing', codes)
    ['drink your ovaltine', 'spooky ghosts', 'spooky scary skeletons']
    '''
    if s == '':
        return []
    ms = []
    if s in d:
        ms.append(d[s])
    for k in range(1, len(s)):
        first, suffix = s[:k], s[k:]
        if first in d:
            for rest in decrypt(suffix, d):
                    ms.append(d[first] + ' ' + rest)
    return ms


def about_equal(t1, t2):
    '''
    >>> x = tree(1, [tree(2), tree(2), tree(3)])
    >>> y = tree(3, [tree(2), tree(1), tree(2)])
    >>> about_equal(x, y)
    True
    >>> z = tree(3, [tree(2), tree(1), tree(2), tree(3)])
    >>> about_equal(x, z)
    False
    '''
    def label_counts(t):
        if is_leaf(t):
            return {label(t):1}
        else:
            counts = {label(t):1}
            branch_counts = [label_counts(branch) for branch in branches(t)]
            for dic in branch_counts:
                for ele in dic:
                    if ele in counts:
                        counts[ele] = counts[ele] + dic[ele]
                    else:
                        counts[ele] = dic[ele]
        return counts
    return label_counts(t1) == label_counts(t2)
