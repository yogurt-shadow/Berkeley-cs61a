def pow(x,y):
    product,k=1,0
    while k<y:
        product,k=product*x,k+1
    return product

def curried_pow(x):
    def h(y):
        return pow(x,y)
    return h

def map_to_range(start,end,g):
    k=start
    while k<=end - 1:
        print(g(k))
        k=k+1

def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g

def uncarry2(g):
    def f(x,y):
        return g(x)(y)
    return f
