def add(n,v):
    return n+v

def test_add():
    assert add(3,2) == 5

if __name__ == '__main__':
    print('запуск файла')
    test_add()