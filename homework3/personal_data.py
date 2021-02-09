def personal(name='', last_name='', year='', city='', email='', phone=''):
    """
Эта функция принимает на вход персональные данные и возвращает их одной строкой
Именованные аргументы:
name - имя
last_name - фамилия
year - год рождения
city - город проживания
email - электронный адрес
phone - мобильный телефон
"""
    return ' '.join([name, last_name, year, city, email, phone])

print(personal(last_name='Юрий', name='Попов', city='1973', year='Москва', phone='matabili1973@gmail.com', email='+7(903)5006247'))
