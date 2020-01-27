"""
Создать вручную и заполнить несколькими строками текстовый файл, 
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки. 
Пример строки файла: firm_1   ООО   10000   5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков). 
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""
import json

with open('lesson_5.7-example.txt') as firms:
    average_list = []
    names = []
    revenues = []
    for line in firms:
        # Лист для удобства работы с разными типа данных
        firm_list = line.split()
        # Звписываем имя в словарь имен
        names.append(firm_list[0])
        # Переводим цифры в формат int
        for i, el in enumerate(firm_list):
            if el.isdigit() == True:
                firm_list[i] = int(el)
        # Считаем прибыль или убыток для каждой фирмы  
        revenue = firm_list[2] - firm_list[3]
        revenues.append(revenue)
        # Но для расчета средней прибыли берем только если фирма осталась в плюсе
        if revenue >= 0:
            average_list.append(revenue)
    average_profit = sum(average_list)
# Собираем словарь и добавляем в него среднюю прибыль
py_dict = dict(zip(names, revenues))
py_dict['average_profit'] = average_profit
# Закидываем словарь в лист
py_list = []
py_list.append(py_dict)
print(py_list)

with open('my_json.json', 'w') as json_f:
    # Для красивой записи используем параметры sort_keys, indent, separators
    # https://docs.python.org/2/library/json.html
    print(json.dumps(py_list, sort_keys=True, indent=4, separators=(',', ': ')), file=json_f)