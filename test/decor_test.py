
def check(func):
    def wrapper(*args):
        if all(isinstance(arg, int) for arg in args):
            result = func(*args)
        else:
            raise TypeError
        return result
    return wrapper
@check
def calc(a,b):
    print(f'+ {a+b}\n - {a-b}\n* {a*b}')

a = int(6)
b = int(5)
calc(a,b)

