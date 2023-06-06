# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9


# n = int(input('Введите колличество кустов: '))
# garden = list()
# for i in range(n):
#     x = int(input('Введите колличество ягод на кусте: '))
#     garden.append(x)
#
# garden_count = list()
# for i in range(len(garden)-1):
#     garden_count.append(garden[i-1] + garden[i] + garden[i+1])
# garden_count.append(garden[-2] + garden[-1] + garden[0])
# print(f'Максимальное число ягод - {max(garden_count)}')


# ---random

# import random
#
# print('Введите количество кустов: ')
# n = int(input())
# garden = []
# for i in range(n):
#     garden.append(random.randint(1, 10))
# print(garden)
# garden_count = []
# for i in range(n-1):
#     summ = garden[i - 1] + garden[i] + garden[i + 1]
#     garden_count.append(summ)
# garden_count.append(garden[-2] + garden[-1] + garden[0])
# print(f'Максимальное число ягод - {max(garden_count)}')

#----- рещение с семинара

# n = int(input())  #  колличество кустов
# array = [int(i) for i in input().split()][:n]  # проходим по всем элеиентам до n
# max_summa = 0 #
# for i in range(1, len(array)-1): # проходим по эементам с 1 до предпоследноего
#     if max_summa < array[i-1] + array[i] + array[i-1]:
#         max_summa = array[i-1] + array[i] + array[i-1]
#
# if max_summa < array[0] + array[1] + array[len(array)-1]:
#     max_summa = array[0] + array[1] + array[len(array) - 1]
# if max_summa < array[0] + array[len(array)-1] + array[len(array)-2]:
#     max_summa = array[0] + array[len(array) - 1] + array[len(array) - 2]
# print(max_summa)


