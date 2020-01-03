"""
Пользователь вводит время в секундах. 
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк.
"""

user_data = int(input('Type your time in seconds:   '))
hours = user_data // 3600
minutes = (user_data - hours * 3600) // 60
seconds = user_data % 60

print('Your time is: {:02}:{:02}:{:02}'.format(hours, minutes, seconds))