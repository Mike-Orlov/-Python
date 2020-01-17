"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.
"""

def person(first_name='first_name', second_name='second_name', date_of_birth='date_of_birth', 
    email='email', tel='tel'):
    print(f'Name: {first_name} {second_name}, birth: {date_of_birth}, contacts: {email}, {tel}')

person(first_name='Mikhail', second_name='Orlov', date_of_birth='03.02.1988', 
    email='ormik@yahoo.com', tel='+7(911)090-91-81')

