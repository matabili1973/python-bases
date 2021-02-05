gains = float(input('Введите сумму выручки в USD:\n'))
costs = float(input('Введите сумму издержек в USD:\n'))

if gains < costs:
    print('Фирма работает в убыток!')
elif gains == costs:
    print('Фирма работает без прибыли!')
else:
    print('Фирма работает с прибылью!')
    print('Рентабельность составляет {:.2f}% от выручки'.format((gains - costs) / gains * 100))
    workers = int(input('Введите количество сотрудников в фирме:\n'))
    print('Получена прибыль в размере {:.2f} USD на каждого сотрудника!'.format((gains - costs) / workers))
