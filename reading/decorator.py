def trace(fn):
    def wrapped(x):
        print('->',fn,'(', x, ')')
        return fn(x)
    return fn
