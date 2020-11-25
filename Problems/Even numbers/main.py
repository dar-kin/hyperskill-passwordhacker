n = int(input())


def even():
    i = 0
    for _j in range(n):
        yield i
        i += 2


# Don't forget to print out the first n numbers one by one here
func = even()
for _i in range(n):
    print(next(func))
