"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, 
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, 
но каждое слово должно начинаться с заглавной буквы. 
Необходимо использовать написанную ранее функцию int_func().
"""

def int_func(string):
    words_list = string.split()
    for i in range(len(words_list)):
        words_list[i] = words_list[i].capitalize()
    return words_list

def int_func2(string):
    '''Capitalize only first letter'''
    words_list = string.split()
    for i in range(len(words_list)):
        string_list = list(words_list[i])
        string_list[0] = string_list[0].capitalize()
        words_list[i] = ''.join(string_list)
    return words_list

print(' '.join(int_func('heLLo wOrlD')))
print(' '.join(int_func2('heLLo wOrlD')))