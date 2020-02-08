"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. 
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад 
и передачу в определенное подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, 
можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, 
нельзя использовать строковый тип данных. 
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, 
изученных на уроках по ООП.
"""
from abc import ABC, abstractmethod

class MyError(Exception):
    def __init__(self, text):
        self.text = text

class Warehouse(ABC):
    item_id = 0
    office_tech = {'Copiers':0, 'Scanners':0, 'Printers':0}
    dept_dict = {}

    @abstractmethod
    def on_board(self):
        """Приемка на склад. 
        
        Метод увеличивает счетчик по соответствующей категории в словаре office_tech.
        И меняет атрибут on_board_status экземпляра на True."""
        pass

    @abstractmethod
    def dept_bond(self):
        """Привязка техники к департаменту.
        
        Принимает имя департамента и присываевает его атрибуту экземпляра. 
        В словарь dept_dict записывается департамент и к-во техники.
        Если деп. новый, то он создается заново, если старый, то просто увеличивается счетчик."""
        pass


class OfficeTech:
    def __init__(self, trademark):
        self.trademark = trademark

class Copier(Warehouse, OfficeTech):
    def __init__(self, trademark, series, warranty_years, color):
        super().__init__(trademark)
        Warehouse.item_id += 1
        self.id = Warehouse.item_id
        self.series = series
        self.warranty_years = warranty_years
        self.color = color
        self.on_board_status = False

    def __str__(self):
        return f'Item copier, id {self.id}, {self.trademark} series {self.series}, color {self.color}'

    def on_board(self):
        Warehouse.office_tech['Copiers'] += 1
        self.on_board_status = True

    def dept_bond(self):
        while True:
            try:
                self.dept = input(f'Input department name for this new {self.trademark} copier id {self.id}: ')
                if self.dept.isalpha() == False:
                    raise MyError('Department should have a correct name')
            except MyError as err:
                print(err)
            else:
                if self.dept in Warehouse.dept_dict:
                    Warehouse.dept_dict[self.dept] += 1
                    break
                else:
                    Warehouse.dept_dict[self.dept] = 1
                    break


class Scanner(Warehouse, OfficeTech):
    def __init__(self, trademark, series, warranty_years, color):
        super().__init__(trademark)
        Warehouse.item_id += 1
        self.id = Warehouse.item_id
        self.series = series
        self.warranty_years = warranty_years
        self.color = color
        self.on_board_status = False
    
    def __str__(self):
        return f'Item scanner, id {self.id}, {self.trademark} series {self.series}, color {self.color}'

    def on_board(self):
        Warehouse.office_tech['Scanners'] += 1
        self.on_board_status = True

    def dept_bond(self):
        while True:
            try:
                self.dept = input(f'Input department name for this new {self.trademark} scanner id {self.id}: ')
                if self.dept.isalpha() == False:
                    raise MyError('Department should have a correct name')
            except MyError as err:
                print(err)
            else:
                if self.dept in Warehouse.dept_dict:
                    Warehouse.dept_dict[self.dept] += 1
                    break
                else:
                    Warehouse.dept_dict[self.dept] = 1
                    break

class Printer(Warehouse, OfficeTech):
    def __init__(self, trademark, series, warranty_years, color):
        super().__init__(trademark)
        Warehouse.item_id += 1
        self.id = Warehouse.item_id
        self.series = series
        self.warranty_years = warranty_years
        self.color = color
        self.on_board_status = False

    def __str__(self):
        return f'Item printer, id {self.id}, {self.trademark} series {self.series}, color {self.color}'

    def on_board(self):
        Warehouse.office_tech['Printers'] += 1
        self.on_board_status = True

    def dept_bond(self):
        while True:
            try:
                self.dept = input(f'Input department name for this new {self.trademark} scanner id {self.id}: ')
                if self.dept.isalpha() == False:
                    raise MyError('Department should have a correct name')
            except MyError as err:
                print(err)
            else:
                if self.dept in Warehouse.dept_dict:
                    Warehouse.dept_dict[self.dept] += 1
                    break
                else:
                    Warehouse.dept_dict[self.dept] = 1
                    break

cop1 = Copier('HP', '1020', 3, "white")
print(cop1)
print(cop1.on_board_status)
cop1.on_board()
print(Warehouse.item_id)
print(cop1.id)
print(cop1.on_board_status)
cop1.dept_bond()
print(cop1.dept)
print(Warehouse.dept_dict)
print(Warehouse.office_tech)
scan1 = Scanner('Asus', 'A54', 2, "grey")
print(scan1)
scan1.on_board()
scan1.dept_bond()
print(scan1.dept)
print(Warehouse.dept_dict)
print(Warehouse.office_tech)