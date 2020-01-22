"""
Представлен список чисел. Определить элементы списка, не имеющие повторений. 
Сформировать итоговый массив чисел, соответствующих требованию. 
Элементы вывести в порядке их следования в исходном списке. 
Для выполнения задания обязательно использовать генератор.

Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

test_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def unique_list(your_list):
    """The function makes new list that contains only unique elements from your list"""
    new_list = []
    for i in your_list:
        if your_list.count(i) > 1:
            pass
        else:
            new_list.append(i)
    yield new_list
    
for el in unique_list(test_list):
    print(el)
