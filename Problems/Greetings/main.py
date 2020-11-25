
def morning(func):
    def wrapper(name):
        func(name)
        print("Good morning,", name)
    return wrapper
