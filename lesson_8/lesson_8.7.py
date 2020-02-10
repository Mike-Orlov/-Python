"""
Реализовать проект «Операции с комплексными числами». 
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта, создав экземпляры класса (комплексные числа) 
и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
"""

class ComplexNumb:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.num = complex(n1, n2)
    def __add__(self, other):
        return f'Сумма чисел: {self.num + other.num}'
    def __mul__(self, other):
        return f'Произведение чисел: {self.num * other.num}'
    def __str__(self):
        return f'Комплексное число {self.n1} + {self.n2}j'

cnum1 = ComplexNumb(1, 2)
cnum2 = ComplexNumb(3, 4)
print(cnum1)
print(cnum2)
print(cnum1 + cnum2)
print(cnum1 * cnum2)