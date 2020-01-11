"""
Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и через dict. 
"""
# Получаем номер месяца от пользователя
while True:
    user_mon = int(input('Type calendar number of the month: '))

    # Защита от неверного номера месяца
    if 1 > user_mon or user_mon > 12:
        print('You should use only natural numbers from 1 to 12. Again...')
    else:
        break

# Готовим словарь для поиска времени года
mon_num = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
season = ['winter', 'spring', 'summer', 'fall']
calendar = dict(zip(season, mon_num))

# Перебираем сезоны (значения ключей в словаре)
for d_season in calendar:
    # Если номер пользователя содержится в значениях ключа, то записываем название ключа в переменную
    if user_mon in calendar[d_season]:
        user_season = d_season
        # Если уже нашли нужный сезон, то для экономии ресурсов прерываем цикл
        break

print(f'Your montn {user_mon} is in {user_season}')