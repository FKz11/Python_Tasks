"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


# Решение через **


def enter(line):
    number = input(line)
    try:
        if line == "Введите число\n>>>:":
            assert float(number) > 0
        if line == "Введите степень\n>>>:":
            assert float(number) < 0 and float(number) % 1 == 0
        return number
    except ValueError:
        return enter(line)
    except AssertionError:
        return enter(line)


def degree(x, y):
    return x ** y


number1 = enter("Введите число\n>>>:")
number2 = enter("Введите степень\n>>>:")
print(degree(float(number1), int(number2)))
