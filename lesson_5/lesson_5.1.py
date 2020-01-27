"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('lesson_5.1-example.txt', 'w') as new_file:
    while True:
        user_str = input('Type what U want to print in a file OR an empty string to quit:\n')
        if user_str == '':
            break
        else:
            print(f'{user_str}', file=new_file)