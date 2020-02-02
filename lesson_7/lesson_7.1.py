"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов 
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица. 
Подсказка: сложение элементов матриц выполнять поэлементно — 
первый элемент первой строки первой матрицы складываем 
с первым элементом первой строки второй матрицы и т.д.
"""
import numpy as np

class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list
    def __str__(self):
        return str(self.matrix_list).replace('], ', ']\n')
    def __add__(self, other):
        try:
            return np.array(self.matrix_list) + np.array(other.matrix_list)
        except ValueError:
            return 'To add matrices use only matrices with equal size!'

matrix1 = Matrix([[3, 4], [1, 6], [3, -1]])
print(matrix1)
print()
matrix2 = Matrix([[0, 4], [9, 3], [3, 6]])
print(matrix2)
print()
print(matrix1 + matrix2)