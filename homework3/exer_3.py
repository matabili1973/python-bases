def my_func(a, b, c):
    """
Эта функция принимает три позиционных аргумента и возвращает сумму двух наибольших из них
Позиционные аргументы:
a, b, c
"""
    if a < b and a < c:
        return b + c
    if b < a and b < c:
        return a + c
    return a + b

x, y, z = [float(x) for x in input('Введите три вещественных числа через пробел:\n').split()]
print(my_func(x, y, z))
