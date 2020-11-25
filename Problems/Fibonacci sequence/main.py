def fibonacci(n):
    if n == 0:
        yield 0
    a = 1
    b = 0
    for _i in range(n):
        if _i == 0:
            yield 0
        elif _i == 1:
            yield 1
        else:
            a, b = a + b, a
            yield a





