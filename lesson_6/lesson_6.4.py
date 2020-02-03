"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: 
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), 
которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        if is_police == False:
            self.is_police = 'Not a police car'
        elif is_police == True:
            self.is_police = 'A police car' 
    def show_speed(self):
        print(f'Current speed is {self.speed}')
    def go(self):
        print('Engine on. Car rides')
    def stop(self):
        print('Engine off. Car stand')
    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} turns {self.direction}')

class TownCar(Car):
    town_limit = 60
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Current speed is {self.speed}')
        if self.speed > TownCar.town_limit:
            print(f'Alarma! Your speed is over limit!')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    work_limit = 40
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Current speed is {self.speed}')
        if self.speed > WorkCar.work_limit:
            print(f'Alarma! Your speed is over limit!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

town = TownCar(65, 'grey', 'Solaris', False)
town.turn('left')
town.show_speed()
print(town.is_police)
print()

sport = SportCar(150, 'red', 'Ferrari', False)
sport.turn('forward')
sport.show_speed()
print(sport.is_police)
print()

work = WorkCar(35, 'yellow', 'Kamaz', is_police=False)
work.turn('right')
work.show_speed()
print(work.is_police)
print()

police = PoliceCar(60, 'special', 'Ford')
police.turn('forward')
police.show_speed()
print(police.is_police)
print()