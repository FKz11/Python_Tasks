"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
revenue = input("Введите выручку фирмы\n>>>: ")
costs = input("Введите издержки фирмы\n>>>: ")
if float(revenue) > float(costs):
    print("Фирма приносит прибыль\n")
elif float(costs) > float(revenue):
    print("Фирма работает в убыток\n")
print("Рентабильность: " + str(float(revenue)/float(costs)))
staff = input("Введите количество сотрудников\n>>>: ")
print("Прибыль фирмы в расчете на одного сотрудника: " + str((float(revenue) - float(costs))/int(staff)))
