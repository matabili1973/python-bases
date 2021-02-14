# Получение списка из вводной строки
my_list = [int(x) for x in input('Введите строку, состоящую из целых чисел, разделенных пробелами:\n').split()]

# Вывод на печать результирующего списка, состоящего из элементов начального списка, значение которых больше значения предыдущих элементов
print([x for x, y in zip(my_list[1:], range(1, len(my_list))) if my_list[y] > my_list[y-1]])
