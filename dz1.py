# 1
# encoding = 'utf-8'
# name = input("Ваше имя: ")
# zp = int(input("Размер зарплаты: "))
# zp = zp*12
# zp = str(zp)
# print(f'{name}, за год получает {zp[:3]}тыс.')

# 2
# number = int(input('Enter number: '))
# if number < 999 and number > 101 and number %2 == 0:
#     print('True')
# else:
#     print('False')

# 3
while True:
    numb = int(input('Enter numb: '))
    if numb == 0:
        break
    if numb < 999 and numb > 101:
        numb = str(numb)
        if numb[-1] == '0':
           numb_conv = numb[::-1]
           print(numb, "->", numb_conv[1:])
        else:
           print(numb, "->",numb[::-1])
    else:
        print('Error number. Try again(101 - 999)')

# 4
# while True:
#
#     num1= int(input("enter numb1: "))
#     num2= int(input("enter numb2: "))
#     op= input("Enter operation(+|-|*|/|%): ")
#     if num1 >= num2:
#             print(f"{num1} >= {num2} = True")
#     else:
#             print(f"{num1} >= {num2} = False")
#     if op == "+":
#             print(f"{num1} + {num2} =", num1 + num2)
#     if op == "-":
#             print(f"{num1} - {num2} =", num1 - num2)
#     if op == "*":
#             print(f"{num1} * {num2} =", num1 * num2)
#     if op == "/":
#             print(f"{num1} / {num2} =", num1 / num2)
#     if op == "%":
#             print(f"{num1} % {num2} =", num1 % num2)

