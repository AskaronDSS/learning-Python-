import requests

def add_numbers(a, b):
    return a + b

def test_add_numbers():
    assert add_numbers(3,2) == 5
    assert add_numbers(-3,-2) == -5
    assert add_numbers(-3,2) == -1
    assert add_numbers(0,2) == 2
    assert add_numbers(5,0) == 5

# Вторая часть задания. Подключиться к АПИ и сделать тест на подключение.
def connect_API(city = 'Kiev', key = '668498292f008dbe9785969c99c8dd16'):
    response = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'
        )
    if response.status_code == 200:
        print('Connect OK')
        return response.status_code
    else:
        raise Exception

def test_conn():
    assert connect_API() == 200