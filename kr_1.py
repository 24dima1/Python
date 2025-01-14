#task 1

def number_cruncing(a, b):
    for i in range(a, b+1):
        print(i)
    return i
number_cruncing(1, 4)

#task 2

def fun_sort(a, b):
    if (a<b):
        for i in range(a, b + 1):
            print(i)
    else:
        for i in range(a,  b-1, -1):
            print(i)
    return i 
fun_sort(2, 1)

#task 3

def fun_sort_odd(a, b):
    for i in range(a, b - 1, -1):
        if i % 2 != 0:
            print(i)
    return i
fun_sort_odd(6, 1)

#task 4

def fun_sum():
    N = int(input(" Введите количество чисел: "))
    sum = 0
    for i in range(0, N):
        sum += int(input(" Введите число: "))
    print(sum)
    return sum
fun_sum()

#task 5

def fun_sum_num():

    N = int(input(" Введите число n: "))
    sum = 0
    for i in range (1, N + 1):
        sum += i ** 3
    print(f"Сумма чисел равна: {sum}")

fun_sum_num()


#task 6

def fun_fact():

    n = int(input(" Введите n факториала: "))
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Сумма чисел равна: {fact} ")

fun_fact()

#task 7

def fun_fact_sum():
    n = int(input("Введите n ряда:"))
    sum = 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        sum += fact
    print(f"Сумма чисел равна: {sum}")
    return sum
fun_fact_sum()

#task 8

def fun_step():
    n = int(input(" Введите n ступенек: "))
    for i in range(1, n + 1):
        step = ""
        for j in range(1, i + 1):
            step += str(j)
        print(step)
    return step
fun_step()

#task 9.1


def fun_sum_fib():
    n = int(input(" Введите количество чисел из ряда Фибоначчи : "))
    fib1, fib2 = 0, 1
    total_sum = 0
    for i in range(n):
        total_sum += fib1
        fib1, fib2 = fib2, fib1 + fib2

    print(f"Сумма чисел равна: {total_sum}")
    return total_sum
fun_sum_fib()

#task 10.1

def fun_sum_fib_num():
    n = int(input(" Введите количество количество чисел из ряда Фибоначчи: "))
    k = int(input(" Введите -порядковый номер в ряду: "))

    fib1, fib2 = 0, 1
    sum = 0
    cur = 1

    for i in range(k + n - 1):
        if cur >= k:
            sum += fib1
        fib1, fib2 = fib2, fib1 + fib2
        cur += 1

    print(f"Сумма чисел равна: {sum}")
    return sum
fun_sum_fib_num()
