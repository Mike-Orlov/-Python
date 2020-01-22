"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. 
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. 
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, work_hours, hour_value, bonus = argv

def zarplata(work_hours=0, hour_value=0, bonus=0):
    return int(work_hours) * int(hour_value) + int(bonus)

print(zarplata(work_hours, hour_value, bonus))