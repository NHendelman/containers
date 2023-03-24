def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]
    '''
    i = -1
    if b is None and c is None:
        while i < (a - 1):
            i += 1
            yield i
    if b is not None and c is None:
        i = (a - 1)
        while i < (b - 1):
            i += 1
            yield i
    if b is not None and c is not None:
        if a < b and c < 0:
            return []
        if a > b and c > 0:
            return []
        if b > 0:
            i = (a - c)
            while (b - i) > 0:
                i += c
                if i <= (b - 1):
                    yield i
        if b < 0:
            i = (a - c)
            while (b - i) < 0:
                i += c
                if i >= (b + 1):
                    yield i
