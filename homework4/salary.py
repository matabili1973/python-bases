from sys import argv

# hours, per_hour, bonus - аргументы, передающиеся через командную строку в виде вещественных чисел
# hours - выработка в часах
# per_hour - почасовая ставка
# bonus - премия

hours, per_hour, bonus = [float(x) for x in argv[1:]]
print('Количество часов: {}\nПочасовая ставка: {}\nПремия: {}'.format(hours, per_hour, bonus))
print('Заработная плата:', hours * per_hour + bonus)
