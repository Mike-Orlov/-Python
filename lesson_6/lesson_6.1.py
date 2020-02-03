"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) 
и метод running (запуск). Атрибут реализовать как приватный. 
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
Продолжительность первого состояния (красный) составляет 7 секунд, 
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.  
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, 
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep
from itertools import cycle

class TrafficLight:
    __color = ['Red', 'Yellow', 'Green', 'Yellow']
    def running(self):
        self.i = 0
        for col in cycle(TrafficLight.__color):
            self.i += 1
            if self.i == 10:
                break
            print(col)
            if col == 'Red':
                sleep(7)
            elif col == 'Yellow':
                sleep(2)
            else:
                sleep(4)

test = TrafficLight()
test.running()  