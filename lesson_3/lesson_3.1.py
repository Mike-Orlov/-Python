"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

# Check if user input is a digit or not. If it's a string while loop repeats.
while True:
    try:
        a = int(input('Type integer A:\n'))
        b = int(input('Type integer B:\n'))
        break
    except ValueError:
        print("ValueError: both values should be digits!")

def division(a, b):
    """The function makes simple division"""
    try:
        print(a / b)
    except ZeroDivisionError:
        print("ZeroDivisionError")
    
division(a, b)
