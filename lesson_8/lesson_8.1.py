"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату 
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. 
Первый, с декоратором @classmethod, должен извлекать число, месяц, год 
и преобразовывать их тип к типу «Число». 
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года 
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

class Date:
    """Class Date() makes objects of dates in string format dd-mm-yyyy"""
    def __init__(self, date):
        Date.date = date

    @classmethod
    def extract_date(cls):
        return [i for i in Date.date.split('-')]

    @staticmethod
    def date_check(date):
        m31 = [1, 3, 5, 7, 8, 10, 12]
        m30 = [4, 6, 9, 11]
        try:
            for i in range(len(date)):
                date[i] = int(date[i])
            if date[2] > 2020:
                raise DateError("Вы ввели не корректно дату!")
            if date[1] in m31:
                if date[0] < 1 or date[0] > 31:
                    raise DateError("Вы ввели не корректно дату!")
            elif date[1] in m30:
                if date[0] < 1 or date[0] > 30:
                    raise DateError("Вы ввели не корректно дату!")
            elif date[1] == 2:
                if date[2] % 4 == 0 and (date[0] < 1 or date[0] > 29):
                    raise DateError("Вы ввели не корректно дату!")
                if date[2] % 4 != 0 and (date[0] < 1 or date[0] > 28):
                        raise DateError("Вы ввели не корректно дату!")
        except ValueError:
            print("Введите дату числами")
        except DateError as err:
            print(err)
        else:
            print('Дата введена корректно')
        finally:
            print(date)

class DateError(Exception):
    def __init__(self, txt):
        self.txt = txt

test = Date('29-02-2019')
Date.date_check(test.extract_date())