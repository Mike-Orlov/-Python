"""
Реализовать два небольших скрипта: 
а) итератор, генерирующий целые числа, начиная с указанного, 
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. 
Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
Необходимо предусмотреть условие его завершения. 
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. 
Во втором также необходимо предусмотреть условие, 
при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle

# Important: in case of infinite loop press 'ctrl + c' to break
digit = int(input('Number to start from:\n'))
stop = 0
for i in count(digit):
    stop += 1
    print(i)
    if stop > 5:
        break

print('----------------------------------------')

# Important: in case of infinite loop press 'ctrl + c' to break
test_list = [2, 'wow', 4.8]
stop1 = 0
for el in cycle(test_list):
    stop1 += 1
    print(el)
    if stop1 > 8:
        break
