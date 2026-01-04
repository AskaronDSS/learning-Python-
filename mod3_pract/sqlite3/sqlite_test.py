number_user = int(input('Enter number: '))
roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
res = ''
for value, ind in roman_map:
    while number_user >= value:
        res += ind
        number_user -= value
print(f'Получится -> {res}')


