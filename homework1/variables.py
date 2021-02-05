myint = int(input('Введите, пожалуйста, целое число:\n'))
print('А это ваше целое число:', myint)

myfloat = float(input('Теперь введите, пожалуйста, число с плавающей точкой:\n'))
print('И вот новое число с плавающей точкой:', myfloat)

print('А теперь посмотрим, равны ли эти числа друг другу:\n', myint == myfloat)

mystr = input('А теперь введите, пожалуйста, строку:\n')
print('Это конкатенация строки и строкового представления целого числа:\n', mystr + str(myint))
print('А это результат умножения строки на целое число:\n', mystr * myint)

mylist = [myint, myfloat, mystr]
print('Это список:', type(mylist), mylist, *mylist, sep = '\n')

mytuple = (myint, myfloat, mystr)
print('А это кортеж:', type(mytuple), mytuple, *mytuple, sep = '\n')

mydict = {'Целое число' : myint, 'Дробное число' : myfloat, 'Строка' : mystr}
print('А это словарь:', type(mydict), mydict, *mydict.items(), sep = '\n')
