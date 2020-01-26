"""
Создать (не программно) текстовый файл со следующим содержимым: 
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""

numbers_dict = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
result = []
with open('lesson_5.4-old.txt') as my_f:
    for line in my_f:
        sp_line = line.split()
        for k, v in numbers_dict.items():
            if k in sp_line[0]:
                sp_line[0] = v
        result.append(' '.join(sp_line))
# Проверка корректности
print(result)

# Без правильной кодировки выдается ошибка при попытке записи
with open('lesson_5.4-new.txt', 'w', encoding='utf-8') as new_f:
    for line in result:
        print(line, file=new_f)