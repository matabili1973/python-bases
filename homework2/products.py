products = []
analytics = {'название' : [], 'цена' : [], 'количество' : [], 'ед' : []}

while True:
    option = input('''Выберите операцию:
1 - добавить запись в базу товаров;
2 - вывести аналитику;
любая другая клавиша - выход.
''')
    if option not in '12':
        break
    elif option == '1':
        print('Введите название, цену, количество товара и единицу измерения:')
        prod = [x for x in input().split()]
        products.append((len(products)+1, {'название' : prod[0], 'цена' : prod[1], 'количество' : prod[2], 'ед' : prod[3]}))
        for index, value in zip(range(len(prod)), analytics.keys()):
            if prod[index] not in analytics[value]:
                analytics[value].append(prod[index])
    else:
        print(analytics)

print(*products, sep = '\n')
