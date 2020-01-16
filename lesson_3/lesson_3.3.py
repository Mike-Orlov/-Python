"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов.
"""

def my_func(a, b, c):
    """The function returns two biggest numbers of three"""
    my_list = [a, b, c]
    lowest = min(my_list)
    my_list.remove(lowest)
    return sum(my_list)

print(my_func(6, 10, 13.2))