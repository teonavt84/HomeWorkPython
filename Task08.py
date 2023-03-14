# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать
# один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

length = int(input('Введите длину шоколадки: '))
width = int(input('Введите ширину шоколадки: '))
piece = int(input('Введите количество долек: '))
if piece == length * width:
    print('Шоколадку необязательно ломать.')
    exit()
chocolate = (length * width) - piece
if chocolate % length == 0 or chocolate % width == 0:
    print("Yes")
else:
    print('No')