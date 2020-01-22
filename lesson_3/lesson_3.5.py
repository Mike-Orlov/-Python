"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, 
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

result = []
def fun_input(*args):
    """The function makes input of digits for who knows why and splits it"""
    args = input('Type your numbers divided with spaces or ^ to quit:\n')
    return args.split()


while True:
    list_of_numbers = fun_input()
    # Check every element of user's tuple
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] == '^':
            print('exit')
            break 
        else:
            digit_number = int(list_of_numbers[i])
            result.append(digit_number)
    if '^' in list_of_numbers:
        break
    print(sum(result))

print(sum(result))

# Другой вариант выхода из while loop:
#
#ex = False
#while ex == False:
#    list_of_numbers = fun_input()
#    for i in range(len(list_of_numbers)):
#        if list_of_numbers[i] == '^':
#            print('exit')
#            ex = True
#            break 
#        else:
#            digit_number = int(list_of_numbers[i])
#            result.append(digit_number)
#    if '^' in list_of_numbers:
#        break
#    print(sum(result))