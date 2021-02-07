seasons = {'winter' : [12, 1, 2], 'spring' : [3, 4, 5], 'summer' : [6, 7, 8], 'autumn' : [9, 10, 11]}
number = int(input('Введите, пожалуйста, целое число в диапазоне от 1 до 12:\n'))

for keyword in seasons.keys():
    if number in seasons[keyword]:
        print(keyword)
