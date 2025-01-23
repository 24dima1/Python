
"""
Для заданий из практической работы №8 для своего варианта.
Организовать ввод данных (матриц) из файла (имя: ФИО_группа_vvod.txt)
И вывод результатов в файл (имя: ФИО_группа_vivod.txt).

"""

import math

def transpose_matrix(matrix):

    n = len(matrix)
    transposed_matrix = [[matrix[j][i] for j in range(n)] for i in range(n)]
    return transposed_matrix


def read_matrix_from_file(filename):
    """Читает данные из файла
    """
    try:
        with open(filename, 'r') as f:
            matrix = []
            for line in f:
                row = [float(x) for x in line.strip().split()]
                matrix.append(row)
            return matrix
    except (FileNotFoundError, ValueError):
        return None


def write_matrix_to_file(matrix, filename):
    """Запись данных в файл.
    """
    try:
        with open(filename, 'w') as f:
            for row in matrix:
                f.write(' '.join(map(str, row)) + '\n')
    except Exception as e:
        print(f"Error writing to file: {e}")


# Присвоение имени и группы
student_name = "Gubin Dmitrii"  # Replace with your name
student_group = "ZIT-24M"  # Replace with your group

input_filename = f"{student_name}_{student_group}_vvod.txt"
output_filename = f"{student_name}_{student_group}_vivod.txt"

# Вызов функции считывающей данные
input_matrix = read_matrix_from_file(input_filename)


if input_matrix:
    transposed_matrix = transpose_matrix(input_matrix)
    if transposed_matrix:
        # Вызов функции записывающей данные
        write_matrix_to_file(transposed_matrix, output_filename)
        print(f"Транспонированная матрица, записа в файл: {output_filename}")
    else:
        print("Неправильный формат входной матрицы")
else:
    print(f"Ошибка считывания матрицы из файла {input_filename}")

