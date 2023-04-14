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

    if b is None and c is None:
        num = 0
        while num < a:
            yield num
            num += 1

    if c is None and b:
        num = a
        while num < b:
            yield num
            num += 1

    if c and b:
        num = a
        if c > 0:
            while num < b:
                yield num
                num += c
        if c < 0:
            while num > b:
                yield num
                num += c
