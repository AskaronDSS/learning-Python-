def check_division_error(func):
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except ZeroDivisionError:
            print("Division by zero")
        except TypeError:
            print("Type error")
    return wrapper

def check_index_error(func):
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except IndexError:
            print("Index out of range")
    return wrapper

@check_division_error
def divine(a,b):
    return a/b

@check_index_error
def get_element(lst, idx):
    return lst[idx]


print(f"Тест ---Divine--- №1\n{divine(5,2)}\n"
      f"Тест ---Divine--- №2\n{divine('5',10)}\n"
      f"Тест ---Divine--- №3\n{divine(5,0)}\n\n")

print(f"Тест ---Get element---№1\n{get_element([1,3,5,12],3)}\n"
      f"Тест ---Get element---№2\n{get_element([1,3],3)}\n")
