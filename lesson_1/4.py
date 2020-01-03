"""
Пользователь вводит целое положительное число. 
Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции.
"""
# Не смог решить без помощи numpy =) А как нужно было?

import numpy as np

chislo = input('Choose positive integer: ')

digits = []
for i in range(len(chislo)):
    digits.append(int(chislo[i]))

digits_np = np.array(digits)
top = digits_np.max()

print(f'The biggest digit in your integer is: {top}')