class A:
    z = -1
    def f(self, x):
        return B(x - 1)

class B(A):
    n = 4
    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y + 1)

class C(B):
    def f(self, x):
        return x
