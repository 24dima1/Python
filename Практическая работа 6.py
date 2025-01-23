#import requests
"""
1 Найдите сумму и произведение элементов списка. Результаты вывести на
экран.

"""
elem = [0]*10
summa = 0
composition = 1
for i in range(10):
    elem[i] = float(input('Введите число '))
    summa += elem[i]
    composition *= elem[i]
print(elem)
print('Сумма = ',summa)
print('Произведение = ',composition)


"""
2 В массиве действительных чисел все нулевые элементы заменить на среднее
арифметическое всех элементов массива.


"""
arr = [1,2,3,0,0,0,0,0,0,5]
avg = sum(arr) / len(arr)
print([avg if x == 0 else x for x in arr])
