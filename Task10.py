'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное
число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите
минимальное количество монет, которые нужно перевернуть
'''
import random
n = int(input('Введите количество монет: '))
array_coin = []
i = 0
j = 0
count_eagle = 0 # орел
count_tails = 0 # решка
while i < n:
    array_coin.append(random.randint(0, 1))
    i = i + 1
for j in array_coin:
    if array_coin[j] == 0:
        count_tails = count_tails + 1
    else:
        count_eagle = count_eagle + 1
if count_tails == 0 or count_eagle == 0:
    print('Переворачивать монеты не нужно.')
    exit()
if count_tails > count_eagle:
    print(f'{count_eagle} монеты необходимо перевернуть')
else:
    print(f'{count_tails} монеты необходимо перевернуть')
