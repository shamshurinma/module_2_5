import random


def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix


n = random.randint(0, 10)  # Вариант задания количества строк рандомно (значения от 0 до 10)
print('Количество строк:', n)
m = random.randint(0, 10)  # Вариант задания количества столбцов рандомно (значения от 0 до 10)
print('Количество столбцов:', m)
value = random.randint(0, 100)  # Вариант задания значения рандомно (значения от 0 до 100)
# n = int(input('Задайте количество строк матрицы: ')) # Вариант задания количества строк вручную
# m = int(input('Задайте количество столбцов матрицы: ')) # Вариант задания количества столбцов вручную
# value = int(input('Задайте значения матрицы: ')) # Вариант задания значения вручную
print('-*-' * m)
matrix = get_matrix(n, m, value)
if n <= 0:
    print('Матрица пуста, задано неверное количество строк:', n)
elif m <= 0:
    print('Матрица пуста, задано неверное количество столбцов:', m)
elif value <= 0:
    print('Матрица пуста!')
    for i in matrix:
        print(*i)
else:
    print('Матрица воплоти:')
    for i in matrix:
        print(*i)