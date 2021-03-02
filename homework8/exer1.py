class Data:

    @classmethod
    def get_data(cls, data):
        result = []
        for element in data.split('-'):
            if element.isdigit():
                result.append(int(element))
            else:
                print('Этот элемент не является числом!')
                return False
        return result

    @staticmethod
    def verify_data(data):
        if not Data.get_data(data):
            print('На проверку передана неправильная дата!')
            return False
        else:
            day, month, year = [x for x in Data.get_data(data)]
            months = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30,
                      7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
            if not year % 400:
                months[2] = 29
            elif year % 100 and not year % 4:
                months[2] = 29
            if 1 > month or 12 < month:
                print('Это неправильный месяц!')
                return False
            if 1 > day or 31 < day:
                print('Это неправильное число!')
                return False
            elif day > months[month]:
                print('В этом месяце нет такого числа!')
                return False
            print('Правильный формат даты!')
            return True

my_data = Data()
print(my_data.get_data('29-02-1972'), Data.verify_data('29-02-1972'))
