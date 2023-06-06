# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def stepen_recursive(a, b):
    if (b==1):
        return a
    if (b != 1):
        return (a*stepen_recursive(a, b-1))

a = int(input('Введите число A: '))
b = int(input('Введите степень B: '))
print(f' => {stepen_recursive(a, b)}')
