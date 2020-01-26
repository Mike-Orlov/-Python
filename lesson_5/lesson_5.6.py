"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает 
учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб)
                    Физика:   30(л)   —   10(лаб)
                    Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

def extract_num(string):
    """The function takes a string, finds digits in it and returns their sum"""
    num_gen = [char for char in string if char.isdigit() == True]
    return ''.join(num_gen)

classes = []
hours = []
with open('lesson_5.6-test.txt') as my_f:
    for line in my_f:
        klass = list(line.split()[0])
        klass.remove(':')
        classes.append(''.join(klass))
        hours_inline = []
        for el in line.split()[1:]:
            if el != '-':
                hours_inline.append(int(extract_num(el)))
        hours.append(sum(hours_inline))

my_dict = dict(zip(classes, hours))
print(my_dict)