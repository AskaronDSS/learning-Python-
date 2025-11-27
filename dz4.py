from datetime import datetime, timedelta
import math
class Examination:

    def __init__(self,n):
        self.n = n
        self.resheto_time = None
        self.any_method_time = None

    def time_n(self):
        return datetime.now()

    def resheto(self):
        time_start = self.time_n()
        prime = [True] * self.n
        prime[0], prime[1] = False, False
        for i in range(2, math.ceil(math.sqrt(self.n))):
            if prime[i]:
                j = i * i
                while j < self.n:
                    prime[j] = False
                    j += i
        primes = [i for i, is_prime in enumerate(prime) if is_prime]
        time_end = self.time_n()
        self.resheto_time = time_end - time_start

    def any_metod(self):
        time_start = self.time_n()
        simples = [2, 3, 5, 7, 11]
        a = 11
        while True:
            b = 0
            a += 1
            for i in range(len(simples)):
                if a % simples[i] == 0:
                    b += 1
            if b == 0:
                simples.append(a)
            if a == self.n:
                break
        time_stop = self.time_n()
        self.any_method_time = time_stop - time_start

    def comparison(self):
        self.resheto()
        self.any_metod()
        resh = self.resheto_time
        an = self.any_method_time
        if resh < an:
            print(f'Проверка с параметром {self.n}\n'
                  f'Время работы метода Решето {resh.microseconds} микросекунд\n'
                  f'Время работы другого метода  {an.microseconds} микросекунд\n'
                  f'Решето быстрее на {an.microseconds - resh.microseconds} микросекунд\n')
        else:
            print(f'Проверка с параметром {self.n}\n'
                  f'Время работы метода Решето {resh.microseconds} микросекунд\n'
                  f'Время работы другого метода  {an.microseconds} микросекунд\n'
                  f'Другой метод быстрее на {an.microseconds - resh.microseconds} микросекунд\n')

test_1 = Examination(100)
test_1.comparison()
test_2 = Examination(1000)
test_2.comparison()