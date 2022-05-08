class Fib:
    '''
    This class represents all the fibonacci numbers,
    but uses O(1) memory to do so.
    >>> list(Fib(5))
    [1, 1, 2, 3, 5]
    '''
    def __init__(self, n=None):
        self.n = n

    def __iter__(self):
        return FibIter(self.n)

    def __repr__(self):
        if self.n:
            return 'Fib(' + str(self.n) + ')'
        else:
            return 'Fib()'


class FibIter:
    '''
    This is the iterator helper class for the Fib class.
    '''
    def __init__(self, n):
        self.n = n
        self.i = 0
        self.f0 = 1
        self.f1 = 1

    def __next__(self):
        if self.n is not None and self.i >= self.n:
            raise StopIteration
        if self.i == 0:
            self.i += 1
            return 1
        elif self.i == 1:
            self.i += 1
            return 1
        else:
            self.i += 1
            self.f2 = self.f0 + self.f1
            self.f0 = self.f1
            self.f1 = self.f2
            return self.f2


def fib_yield(n=None):
    '''
    This function returns a generator that computes the first n fibonacci numbers.
    If n is None, then the generator is infinite.
    '''
    f0 = 1
    f1 = 1
    yield 1
    if n == 1:
        return
    yield 1
    if n == 2:
        return
    i = 3
    while True:
        f2 = f0 + f1
        yield f2
        f0 = f1
        f1 = f2
        i += 1
        if n is not None and i > n:
            return
