#import requests
"""
Найти все натуральные числа, не превосходящие заданного n, которые
делятся на каждую из своих цифр.

"""
n = int(input("Введите натуральное число n: "))

for num in range(1, n+1):
    is_divisible = True
    digits = str(num)
    for digit in digits:
        if digit != '0' and num % int(digit) != 0:
            is_divisible = False
            break
    if is_divisible:
        print(num, end=' ')

"""
2 Ввести одномерный массив A длиной m. Поменять в нём местами первый и
последний элементы. Длину массива и его элементы ввести с клавиатуры. В
программе описать процедуру для замены элементов массива. Вывести
исходные и полученные массивы.

"""
def func1(a):
    a[0], a[-1] = a[-1], a[0]
    return a


n = int(input('m = '))
a = list(map(int, input('в одну строку через пробел ').split(maxsplit=n)))

print(a)
print(func1(a))

