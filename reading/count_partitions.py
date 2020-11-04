'''
The number of ways to partition n using integers up to m equals
the number of ways to partition n-m using integers up to m, and
the number of ways to partition n using integers up to m-1.
(n, m) = (n, m-1) + (n-m, m)
'''
def count_partitions(n,m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)
