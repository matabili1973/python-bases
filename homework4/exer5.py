from functools import reduce

def multiply(arg1, arg2):
    """
Эта функция возвращает произведение двух переданных аргументов
arg1, arg2 - позиционные аргументы в виде вещественных чисел
"""
    return arg1 * arg2

print(reduce(multiply, [x for x in range(100, 1001, 2)]))
