#import requests
"""
натуральные числа Х,N Вычислить выражение вида: x^n / n!.
"""

def f(x,n):
    def fac(n):
        if n<1:
            return 1
        else:
            return n * fac(n-1)
    return x**n/fac(n)
print(f(4,5))

"""
Дано натуральное число n>1. Проверьте, является ли оно простым.
Программа должна вывести слово YES, если число простое и NO, если
Число составное. Алгоритм должен иметь сложность O(logn).
Указание. Понятно, что задача сама по себе нерекурсивна, т.к. проверка
числа n на простоту никак не сводится к проверке на простоту меньших
чисел. Поэтому нужно сделать еще один параметр рекурсии: делитель
числа, и именно по этому параметру и делать рекурсию.
"""

def recursion(n, i):
        # i- дополнительный параметр. При вызове должен быть равен 2
        # Базовый случай
        if (n < 2):
            return 'No'
        # Базовый случай
        elif n == 2:
            return 'Yes';
        # Базовый случай
        elif (n % i == 0):
            return 'No';
        #Шаг рекурсии / рекурсивное условие
        elif (i < n / 2):
            return recursion(n, i + 1);
        else:
            return 'Yes'

print(recursion(22, 2))
