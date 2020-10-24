"""
2. Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""


def enter(line):
    numbers = input(line).split(' ')
    try:
        for i in numbers:
            float(i)
        return numbers
    except ValueError:
        return enter(line)


my_list = enter("Введите числа через пробел\n>>>:")
new_list = [a for a in my_list[1:] if float(a) > float(my_list[my_list.index(a) - 1])]
print(*new_list)
