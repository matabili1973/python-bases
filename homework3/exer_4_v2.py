def my_func(base, indic):
    if not indic:
        return 1
    return my_func(base, indic + 1) / base

a = float(input('Введите любое положительное число:\n'))
b = int(input('Введите целое отрицательное число:\n'))

print(my_func(a, b))
