"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
name, surname, position (должность), income (доход). 
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: 
оклад и премия, например, {"wage": wage, "bonus": bonus}. 
Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
и дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, 
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage':wage, 'bonus':bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        print(f"Worker's full name is {self.name} {self.surname} and he is {self.position}")
    def get_total_income(self):
        self.total_income = self._income['wage'] + self._income['bonus']
        print(f"Worker's total income is {self.total_income}")

petya_pos = Position('Pavel', 'Durov', 'CEO', 100000, 80000)
print(petya_pos.name)
print(petya_pos.surname)
print(petya_pos.position)
petya_pos.get_full_name()
petya_pos.get_total_income()