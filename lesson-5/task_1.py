"""
1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open('task_1_write.txt', 'w', encoding='UTF=8') as file:
    my_line = input("Введите строку в файл или пустую строку для остановки\n>>>:")
    while my_line != '':
        file.write(my_line + '\n')
        my_line = input("Введите строку в файл или пустую строку для остановки\n>>>:")