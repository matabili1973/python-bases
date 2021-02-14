my_list = [int(x) for x in input('Введите ряд целых чисел через пробел:\n').split()]
print([x for x in my_list if my_list.count(x) == 1])
