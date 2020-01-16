"""
Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. 
Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. 
Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

def my_func(x, y):
    """The function raises X to the power of Y with operator **"""
    return x ** y

print(my_func(2, -3))

def my_func2(x, y):
    """The function raises X to the power of Y with for-loop"""
    x_v_stepeni_y = 1
    # Multiplication Y times
    for i in range(abs(y)):
        x_v_stepeni_y *= x
    return 1 / x_v_stepeni_y

print(my_func2(2, -3))