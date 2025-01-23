#import requests
"""
1 Задана матрица порядка n и число к. Разделить элементы k-й строки
на диагональный элемент, расположенный в этой строке.

"""
n = int(input("Введите n: "))

k = int(input("Введите k: "))

arr = [[int(input()) for j in range(n)] for i in range(n)]

for i in range(n):

   for j in range(n):

       if k == i:

           arr[i][j] = arr[i][j] / arr[i][i]

"""
Задана квадратная матрица. Получить транспонированную матрицу
(перевернутую относительно главной диагонали) и вывести на экран.

"""


def transpose_matrix(matrix):
    n = len(matrix)
    transposed_matrix = [[matrix[j][i] for j in range(n)] for i in range(n)]

    return transposed_matrix


# Example Usage:
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result1 = transpose_matrix(matrix1)

if result1:
  print("Original matrix:")
  for row in matrix1:
    print(row)
  print("\nTransposed matrix:")
  for row in result1:
    print(row)

