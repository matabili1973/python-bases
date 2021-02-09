def my_func(a, b, c):
    """
Эта функция принимает три позиционных аргумента и возвращает сумму двух наибольших из них
Позиционные аргументы:
a, b, c
"""
    my_list = sorted([a, b, c])
    return my_list[1] + my_list[2]

x, y, z = [float(x) for x in input('Введите три вещественных числа через пробел:\n').split()]
print(my_func(x, y, z))
