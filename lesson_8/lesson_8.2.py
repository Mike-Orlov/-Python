"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию 
и не завершиться с ошибкой.
"""

class NullError(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    try:
        user_num1 = int(input('Input a divident:\n'))
        user_num2 = int(input('Input a divider (spoiler: use zero for custom error):\n'))
        if user_num2 == 0:
            raise NullError("You shouldn't divide by zero!")
    except NullError as err:
        print(err)
        break
    except ValueError:
        print('ValueError - input a number, please')
    else:
        print(f'{user_num1} / {user_num2} = {user_num1 / user_num2}\nbut the only way to quit is to make zero division =)\n|\nV')