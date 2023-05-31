# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# # ----------- ручной ввод
# n = int(input('Введите колличество монет: '))
# count1 = 0 # решка
# count2 = 0 # орел
#
# for i in range(n):
#     temp = int(input())
#     if temp == 0:
#         count1 += 1
#     elif temp == 1:
#         count2 += 1
# print(f'решка => {count1} - орел => {count2}')
# if count1 < count2:
#     print(f'необходимо перевернуть {count1} решка')
# else:
#     print(f'необходимо перевернуть {count2} орел')

# # ----------- рандомный ввод
# n = int(input('Введите колличество монет: '))
# count1 = 0 # решка
# count2 = 0 # орел
#
# for i in range(n):
#     temp = random.randint(0,1)
#     print(temp, end=' ')
#     if temp == 0:
#         count1 += 1
#     elif temp == 1:
#         count2 += 1
# print(f'решка => {count1} - орел => {count2}')
# if count1 < count2:
#     print(f'необходимо перевернуть {count1} решка')
# else:
#     print(f'необходимо перевернуть {count2} орел')

#--еще 1 вариант

# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
# x = int(input())
# if x == 0:
# count_zero += 1
# else:
# count_one += 1
# if count_one > count_zero:
# print(count_zero)
# else:
# print(count_one)