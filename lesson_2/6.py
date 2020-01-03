"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с параметрами 
(характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры: 
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}
"""

# Готовим пустой лист и значения ключей
goods = []
goods_keys = ['Item name', 'Item price', 'Quantity in stock', 'Units of measure']
index = 0

# Цикл while, чтобы проводить запрашивать столько раз, сколько хочет пользователь
while True:
    ask = input('Do you want to add an item? (y/n) ')
    if ask == 'y':
        # Номер вводимой позиции
        index += 1
        # Последовательно запрашиваю атрибуты товара
        item_name = input('Item name: ')
        item_price = input('Item price: ')
        item_instock = input('Quantity in stock: ')
        item_instock_units = input('Units of measure: ')
        goods_values = [item_name, item_price, item_instock, item_instock_units]
        item = dict(zip(goods_keys, goods_values))
        # В конце каждого цикла записываю в лист goods словарь с товаром
        goods.append((index, [item]))
        # Для удобства вывожу только что добавленный товар
        print()
        print(f'Just added to goods:\n{item}\n')
        continue
    elif ask == 'n':
        print()
        break
    else:
        print("Wrong answer")

print('Total rows of goods in stock:')
for item in goods:
    print(item)
print()

# Не придумал умнее, чем создать под каждую пременную лист и туда собирать значения
i = 0
item_name_all = []
item_price_all = []
item_instock_all = []
item_instock_units_all = []

# Цикл проходит по всем индексам, в зависимости от длины листа goods 
# Т.е. сколько товаров ввел пользователь, столько раз цикл пройдет по листу goods
while i < len(goods):
    # Из каждого товара в соотв. переменные добавляются значения ключей
    item_name_all.append([goods[i][1][0]['Item name']])
    item_price_all.append([goods[i][1][0]['Item price']])
    item_instock_all.append([goods[i][1][0]['Quantity in stock']])
    item_instock_units_all.append([goods[i][1][0]['Units of measure']])
    i += 1

# Собираем словарь
analitics_values = [item_name_all, item_price_all, item_instock_all, item_instock_units_all]
result_analitics = dict(zip(goods_keys, analitics_values))

# Не знаю, как вывести словарь построчно, поэтому кастую его в лист и циклом вывожу по строкам
result_pretty = result_analitics.items()

for key in result_pretty:
    print(key)