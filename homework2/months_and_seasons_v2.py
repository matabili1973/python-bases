winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]
number = int(input('Введите, пожалуйста, целое число в диапазоне от 1 до 12:\n'))

if number in winter:
    print('winter')
elif number in spring:
    print('spring')
elif number in summer:
    print('summer')
elif number in fall:
    print('fall')
