'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''
n = int(input('Введите число N: '))
i = 0
print(f'Целые степени двойки до числа {n}')
while 2 ** i <= n:
    print(2 ** i)
    i = i + 1