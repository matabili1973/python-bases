# Вводится целое положительное число
number = int(input('Введите целое положительное число:\n'))

# Счетчик самого большого числа
result = 0

# Цикл перебора цифр числа с единиц к старим разрядам
while number > 0:
    while result < number % 10:
        result = number % 10
    number = number // 10

print(result)
