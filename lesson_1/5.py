"""
Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, 
или убыток — издержки больше выручки). Выведите соответствующее сообщение. 
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

revenue = int(input('Revenue: '))
losses = int(input('Costs: '))

if (revenue - losses) > 0:
    print('You make profit')
    print(f'ROI = {((revenue - losses) / revenue):.2%}')
    personal = int(input('Number of employees: '))
    print(f'Profit per 1 employee is: {((revenue - losses) / personal):.2f}')
else:
    print('You make losses')

