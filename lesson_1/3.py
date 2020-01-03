"""
Узнайте у пользователя число n. 
Найдите сумму чисел n + nn + nnn. 
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

n = input('Choose your number:  ')

n_sum = int(n) + int(n + n) + int(n + n + n)

print(f'Result of {n} + {n + n} + {n + n + n} is: {n_sum}')