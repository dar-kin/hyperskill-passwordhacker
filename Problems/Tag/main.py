def tagged(func):
    def wrapper(inp):
        return "<title>" + func(inp) + "</title>"
    return wrapper
