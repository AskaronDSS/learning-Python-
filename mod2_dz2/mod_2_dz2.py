import numpy as np
#1_1
rand_5 = np.random.randint(10, size=(5,5))
rand_5_2 = np.random.randint(10, size=(5,5))

sum_rand_5 = rand_5.sum()
sum_rand_5_2 = rand_5_2.sum()
print(f'Сумма елементов первого массива -> {sum_rand_5}\n'
      f'Сумма елементов второго массива -> {sum_rand_5_2}')

#1_2
razn = rand_5_2 - rand_5
print(f'Разница ->\n {razn}\n')
#1_3
res_dobutok = rand_5_2 * rand_5
print(f'Результат умножения  ->\n{res_dobutok}\n')
#1_4
res_pow = np.zeros((5,5), dtype = float)
for i in range(5):
    for j in range(5):
       res_pow[i][j] = rand_5[i][j] ** rand_5_2[i][j]
print(f'Возведение в степень -> \n{res_pow}')

#2
doska = np.zeros((8,8))
for i in range(0,8):
    for s in range(0,8):
        if (i + s) % 2 == 0:
            doska[i][s] = 0
        else:
            doska[i][s] = 1
print(doska)
#2_1
print(f'Третий ряд с шахматной доски -> {doska[2]}')
#2_2
print(f'Пятый столбик с шахматной доски -> {doska[:,4]}')
#2_3
#Я не правильно прочитал задание.
# Прочитал и счегото в голове отложилось,
# что нужно массив 3х3 сверху с права...
mass_mini = doska[0:3,0:3]
print(f'Подмассив из массива 8х8(шахматная доска)\n{mass_mini}')



