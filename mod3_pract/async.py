from concurrent.futures import ThreadPoolExecutor
import datetime
import random
import threading
import time
# def decor(func):
#     def wrapper(*args, **kwargs):
       
#         start = datetime.datetime.now()
#         print(start)
#         result = func(*args, **kwargs)
#         end = datetime.datetime.now()
#         print(end)
#         return result
#     return wrapper

# @decor
# def factory(a):
#     summa = 1
#     for i in range(1,a):
#         summa *= i
#     print(summa)

# thread = threading.Thread(target=factory, args = (10,))
# thread.start()

# thread2 = threading.Thread(target=factory, args= (20,))
# thread2.start()



# Створи змінну counter = 0, два потоки, кожен збільшує її 100000 разів. 
# Покажи, що результат не дорівнює 200000. Потім виправ за допомогою Lock.


# counter = 0


# def plus():
#     global counter
#     counter += 1
#     print(counter)

# for _ in range(100000):
#     thread1 = threading.Thread(target=plus)
#     thread2 = threading.Thread(target=plus)

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()
# else:
#     print("Done")


# мітуй рахунок та два потоки, що намагаються зняти гроші одночасно. 
# Без Lock → помилка балансу. З Lock → правильно.

# balance = 1000
# # lock = threading.Lock()
# def minus(a):
#     global balance
#     print(f'Начало -> {balance}')
#     # with lock:
#     if balance > 0:
#         time.sleep(0.1)
#         balance -= a
#     print(f'Конец -> {balance}')
#     return balance
# for _ in range(10):
   
#     thread1 = threading.Thread(target=minus, args=(80,))
    
#     thread2 = threading.Thread(target=minus, args=(2,))
#     print('поток 1')
#     thread1.start()
#     print('поток 2')
#     thread2.start()

#     thread1.join()
#     thread2.join()

# print(f'Итоговый баланс -> {balance}')


# Створи чергу із 10 чисел. 
# 3 робочих потоки (workers) мають брати число з черги, обчислювати квадрат
# і друкувати результат.

# cherga = [1,2,3,4,5,6,7,8,9,10]
# lock = threading.Lock()
# def workers():
#     global cherga
#     while cherga:
#         with lock:
#             if cherga:
#                 num = cherga.pop(0)
#                 print(f'Квадрат числа {num} -> {num ** 2}')
#             else:
#                 return
            

# thread1 = threading.Thread(target=workers)
# thread2 = threading.Thread(target=workers)
# thread3 = threading.Thread(target=workers)

# thread1.start()
# thread2.start()
# thread3.start()

# thread1.join()
# thread2.join()
# thread3.join()


event = threading.Event()

def wait_for_event():
    print("Чекаю на подію...")
    event.wait()
    print("Подія сталася!")

def set_event():
    print("Подія встановлена.")
    event.set()

thread1 = threading.Thread(target=wait_for_event)
thread2 = threading.Thread(target=set_event)

thread1.start()
thread2.start()