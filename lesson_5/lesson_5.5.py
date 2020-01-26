"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint

rand_gen = [randint(0, 50) for i in range(0, 10)]
print(f'Sequence (random): {rand_gen}')
with open('lesson_5.5-test.txt', 'w') as my_f:
    new_content = " ".join(str(rand_gen))
    print(new_content, file=my_f)
print(f'Sum of numbers: {sum(rand_gen)}')