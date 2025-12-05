import threading
import queue
import time
def decor_time(func): # Декоратор для замера потраченого времени на работу функции
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        res_time = end_time - start_time
        print(f'Время выполнения {func.__name__}: {res_time:.5f} секунд')
        return result
    return wrapper


def is_prime(n): # Задание 1. Проверка на простое число
    if n < 2: # Простые числа начинаются с 2
        return False
    for i in range(2, int(n**0.5) + 1): # Проверка на делитель кроме 1 и самого числа
        if n % i == 0:
            return False
    return True
#Тесты функции is_prime
# Простые числа от 2 - 50.
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47.
print(f'Тест 1. Проверка числа 11: {is_prime(11)}\n'
      f'Тест 2. Проверка числа 7: {is_prime(7)}\n'
      f'Тест 3. Проверка числа 35: {is_prime(35)}\n'
      f'Тест 4. Проверка числа 36: {is_prime(36)}\n'
      f'Тест 5. Проверка числа 37: {is_prime(37)}\n')
@decor_time
def find_primes_single_tread(start, end, q=None, name = 'Один поток'): #Задание 2. Поиск простых чисел в диапазоне start-end
    result = [] #будет собирать простые числа
    lock = threading.Lock()
    for number in range(start, end+1):# перебор всех чисел в заданном диапазоне
        if is_prime(number):# проверка на простое число
            result.append(number)
    with lock:
        print(f'{name} ->\n{result}')
        if q is not None:
            q.put(result)
    return result
# Запуск одного потока. От 1 до 100
thread = threading.Thread(target=find_primes_single_tread, args=(1,100))
thread.start()

@decor_time
def find_primes_multi_thread(start, end, name_two = None): #Задание 3. Поиск простых чисел в диапазоне start-end с использованием двух потоков
    result = []
    lock = threading.Lock()
    name_two = 'Два потока'
    q = queue.Queue()
    end_one = (start + end) // 2 # находим середину диапазона
    # создаем два потока для поиска простых чисел
    
    one_stream = threading.Thread(target=find_primes_single_tread, args=(start, int(end_one), q, 'Первый поток'))
    two_stream = threading.Thread(target=find_primes_single_tread, args=(int(end_one), end, q, 'Второй поток'))
    one_stream.start() 
    two_stream.start() 
    one_stream.join() 
    two_stream.join()
    with lock:
        while not q.empty(): # собираем результаты из очереди. Путем обьединения списков
            result.extend(q.get()) 

        print(f'{name_two}->\n{result}')

find_primes_multi_thread(1,100)


# В итоге, оба варианта (один поток и два потока) выдают одинаковый результат - список простых чисел от 1 до 100.
# Судя по замерам времени работы, можно сделать вывод, 
# что, хотя мы и разделили нагрузку на два потока, 
# Python переключается между ними, и в итоге общее время выполнения увеличивается.
