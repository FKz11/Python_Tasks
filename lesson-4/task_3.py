"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""


def my_range(start, end):
    while start < end:
        yield start
        start += 1


print(*[a for a in my_range(20, 241) if a % 20 == 0 or a % 21 == 0])
