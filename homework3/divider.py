def divider(a, b):
    """
Возвращает результат деления первого аргумента на второй
Позиционные аргументы:
a - делимое
b - делитель
"""
    if b == 0:
        return 'This is not a valid operation.'
    return a / b

x, y = float(input()), float(input())
print(divider(x, y))
