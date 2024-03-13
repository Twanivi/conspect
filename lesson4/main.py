# 1) == - равенство
# 2) != -не равно
# 3) > - больше
# 4) < - меньше
# 5) >= - больше либо равно
# 6) <= - меньше либо равно

# print(5 == 5)
# print(5 != 5)
# print(5 > 4)
# print(5 < 6)
# print(5 >= 5)
# print(5 <= 4)

# if  условие:
# табуляция(4 пробела) + код проги
# elif условие:
# таб + код
# else:
# табуляция + код

# x = 10
# if x < 5:
#     print('if был выполнен')
# elif x == 10:
#     print('elif был выполнен')
# else:
#     print('else был выполнен')

# and - и
# or - или
# not - не
# not True = False
# not False = True

# x = 4
# if x == 10 and x > 5:
#     print('выполнение and')
# elif x == 4 or x> 5:
#     print('выполнение or')

# x = int(input('Введите число: '))
# if x % 2 != 0:
#     print('Число', x, 'нечётное')
# else:
#     print('Число', x, 'чётное')

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# c = int(input('Введите третье число: '))
#
# if a > b and a > c:
#     print('Число', a, 'наибольшее')
# elif b > c:
#     print('Число', b, 'наибольшее')
# else:
#     print('Число', c, 'наибольшее')

# x = int(input('Введите число: '))
# if x < 100 and x > -100:
#     print('+')
# else:
#     print('-')

# x = float(input('Введите первое число: '))
# operator = input('Введите действие: ')
# y = float(input('Введите второе число: '))
#
# if operator == '*':
#     print('Произведение =', x * y)
# elif operator == '/':
#     print('Частное =', x / y)
# elif operator == '+':
#     print('Сумма =', x + y)
# else:
#     print('Разность =', x - y)
#
# degree = int(input('Введите температуру, °C: '))
# if degree < 0:
#     print('На улице холодно')
# else:
#     print('На улице тепло')

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))

if x % y == 0:
    print('Число', x, 'кратно', y)
else:
    print('Число', x, 'некратно', y)
