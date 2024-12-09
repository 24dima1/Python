#task 1
a = 1
b = 2
for i in range(a, b+1):
    print(i)

#task 2
a = 2
b = 1
if (a<b):
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a,  b-1, -1):
        print(i)
#task 3
a = 6
b = 1
for i in range(a, b - 1, -1):
    if i % 2 != 0:
        print(i)
#task 4
N = int(input(" Введите количество чисел: "))
sum = 0
for i in range (0, N):
    sum += int(input(" Введите число: "))
print(sum)

#task 5

N = int(input(" Введите число n: "))
sum = 0
for i in range (1, N + 1):
    sum += i ** 3
print(f"Сумма чисел равна: {sum}")

#task 6
n = int(input(" Введите n факториала: "))
fact = 1
for i in range (1, n + 1):
    fact *= i
print(f"Сумма чисел равна: {fact} ")

#task 7
n = int(input("Введите n ряда:"))
sum = 0
fact = 1
for i in range (1, n + 1):
    fact *= i
    sum += fact
print(f"Сумма чисел равна: {sum}" )

#task 8
n = int(input(" Введите n ступенек: "))
for i in range(1, n + 1):
        step = ""
        for j in range(1, i + 1):
            step += str(j)
        print(step)

#task 9

n = int(input(" Введите количество чисел из ряда Фибоначчи : "))
fib1, fib2 = 0, 1
total_sum = 0
for i in range(n):
    total_sum += fib1
    fib1, fib2 = fib2, fib1 + fib2

print(f"Сумма чисел равна: {total_sum}")

#task 10

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
