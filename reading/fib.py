def fib(n):
    '''
    pre,cur
    n begins from 1
    '''
    pre,cur=0,1
    k=2
    while k<n:
        pre,cur=cur,pre+cur
        k=k+1
    return cur
