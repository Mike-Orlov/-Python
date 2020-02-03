"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. 
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, 
необходимого для покрытия всего дорожного полотна. 
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, 
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""

class Road:
    kg_asphalt_nametr = 25
    tolschina_sm = 5
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.tonna_mass = Road.kg_asphalt_nametr * Road.tolschina_sm * self._length * self._width
    def asf_mass(self):
        return f'You need {self.tonna_mass / 1000:.1f} tons of asphalt for the project'

new_shosse = Road(20, 5000)
print(new_shosse.asf_mass())

