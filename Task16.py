'''
Задача 16:
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
Заполните массив случайными натуральными числами от 1 до N/2.
Выведите, сколько раз X встречается в массиве.

Ввод: 5
Ввод: 1

1 2 1 2 2
Вывод: 2
'''
import random
len_list = int(input('Введите длину массива: '))
num = int(input('Введите искомое число: '))
list = []
count = 0
for i in range(len_list):
    list.append(random.randint(1, int(len_list / 2)))
print(list)
for j in list:
    if j == num:
        count = count + 1
print(f'Цифра {num} встречается {count} раз.')