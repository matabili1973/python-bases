def my_func(base, indic):
    result = 1
    for counter in range(-1, indic - 1, -1):
        result /= base
    return result

a = float(input('Введите любое положительное число:\n'))
b = int(input('Введите целое отрицательное число:\n'))

print(my_func(a, b))
