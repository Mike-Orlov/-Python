"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_file = 'lesson_5.2-example.txt'

with open(my_file, 'r') as ipsum:
    strings = 0
    for line in ipsum:
        strings +=1
    # Should return coursor to start
    ipsum.seek(0)
    # Separete words with method .split()
    words_list = ipsum.read().split()

print(f"The text file contains {strings} strings\nAnd there're {len(words_list)} in it")