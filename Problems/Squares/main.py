n = int(input())


def squares(a):
    i = 1
    for _elem in range(a):
        yield i ** 2
        i += 1


# Don't forget to print out the first n numbers one by one here
func = squares(n)
for _i in range(n):
    print(next(func))
