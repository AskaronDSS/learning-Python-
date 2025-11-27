# 1
# while True:
#     try:
#         test = int(input('Enter numb: '))
#         if test%3==0 and test%5==0:
#             print('ham')
#         elif test%5 == 0:
#             print('bar')
#         elif test%3 == 0:
#             print('foo')
#
#     except ValueError:
#         print('Enter integer!')
#     except TypeError:
#         print('Please, enter integer!')

# 2
# while True:
#     try:
#         num = float(input("Get: "))
#         num2 = float(input("Get 2: "))
#         if num > num2:
#             print(f'Large number = {num}\n'
#                   f'Smaller number = {num2}')
#         else:
#             print(f'Large number = {num2}\n'
#                   f'Smaller number = {num}')
#     except ValueError:
#         print('Please enter number')

# 3
# triger = True
# while triger:
#     try:
#         num = float(input('Get: '))
#         num2 = float(input('Get 2: '))
#         num3 = float(input('Get 3: '))
#     except ValueError:
#         print('You must enter integer/float')
#         continue
#     triger = False
#     res = [num,num2,num3]
#     res = sorted(res)
#     print(f'min number = {res[0]}\n'
#           f'number = {res[1]}\n'
#           f'max number = {res[-1]}'
#           )
# 4
# test = list(range(1,101))
# for x in test:
#     if x%3==0 and x%5==0:
#         print('fizz buzz')
#     elif x%5 == 0:
#         print('Buzz')
#     elif x%3 == 0:
#         print('fizz')
#     else:
#         print(x)


# 5
# numb = range(1,101)
# for x in numb:
#     if x%7==0 or '7' in str(x):
#         print('BOOM')
#     else:
#         print(x)

