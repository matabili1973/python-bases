class Store:

    def __init__(self):
        self.printers = {}
        self.scanners = {}
        self.xeroxes = {}

    def get_tech(self, item):
        if item['Тип устройства'] == 'Принтер':
            try:
                item['Розничная цена'] = float(item['Розничная цена'])
                item['Количество'] = int(item['Количество'])
            except ValueError:
                print('Вы вводите не число!')
                return False
            self.printers['PRN' + str(len(self.printers))] = item
        elif item['Тип устройства'] == 'Сканер':
            try:
                item['Розничная цена'] = float(item['Розничная цена'])
                item['Количество'] = int(item['Количество'])
            except ValueError:
                print('Вы вводите не число!')
                return False
            self.scanners['SCN' + str(len(self.scanners))] = item
        else:
            try:
                item['Скорость черно-белого копирования, страниц в минуту'] = int(item['Скорость черно-белого копирования, страниц в минуту'])
                item['Скорость цветного копирования, страниц в минуту'] = int(item['Скорость цветного копирования, страниц в минуту'])
                item['Розничная цена'] = float(item['Розничная цена'])
                item['Количество'] = int(item['Количество'])
            except ValueError:
                print('Вы вводите не число!')
                return False
            self.xeroxes['XRS' + str(len(self.xeroxes))] = item

    def send_item(self, key):
        if key in self.printers.keys():
            Department.printers[key] = self.printers[key]
            del(self.printers[key])
        elif key in self.scanners.keys():
            Department.scanners[key] = self.scanners[key]
            del(self.scanners[key])
        else:
            Department.xeroxes[key] = self.xeroxes[key]
            del(self.xeroxes[key])

    def recover_item(self, key):
        if key in Department.printers.keys():
            self.printers[key] = Department.printers[key]
            del(Department.printers[key])
        elif key in Department.scanners.keys():
            self.scanners[key] = Department.scanners[key]
            del(Department.scanners[key])
        else:
            self.xeroxes[key] = Department.xeroxes[key]
            del(Department.xeroxes[key])


class Department:
    printers = {}
    scanners = {}
    xeroxes = {}


class Tech:
    
    def __init__(self, device, manufactor, model, color, size, price, quantity):
        self.device = device
        self.manufactor = manufactor
        self.model = model
        self.color = color
        self.size = size
        self.price = price
        self.quantity = quantity


class Printer(Tech):
    
    def __init__(self, *args, technology = 'не указана'):
        self.technology = technology
        super().__init__('Принтер', *args)

    def unit(self):
        return {
            'Тип устройства': self.device,
            'Изготовитель': self.manufactor,
            'Модель': self.model,
            'Технология печати': self.technology,
            'Цветность печати': self.color,
            'Формат бумаги': self.size,
            'Розничная цена': self.price,
            'Количество': self.quantity
            }


class Scanner(Tech):

    def __init__(self, *args, scanner_type = 'не указан'):
        self.scanner_type = scanner_type
        super().__init__('Сканер', *args)

    def unit(self):
        return {
            'Тип устройства': self.device,
            'Изготовитель': self.manufactor,
            'Модель': self.model,
            'Тип сканера': self.scanner_type,
            'Цветность сканирования': self.color,
            'Формат бумаги': self.size,
            'Розничная цена': self.price,
            'Количество': self.quantity
            }


class Xerox(Tech):

    def __init__(self, *args, bw_speed = 'не указана', color_speed = 'не указана'):
        self.bw_speed = bw_speed
        self.color_speed = color_speed
        super().__init__('Копир', *args)

    def unit(self):
        return {
            'Тип устройства': self.device,
            'Изготовитель': self.manufactor,
            'Модель': self.model,
            'Цветность копирования': self.color,
            'Формат бумаги': self.size,
            'Скорость черно-белого копирования, страниц в минуту': self.bw_speed,
            'Скорость цветного копирования, страниц в минуту': self.color_speed,
            'Розничная цена': self.price,
            'Количество': self.quantity
            }


a = Xerox('Ricoh', 'DD 3840C', 'цветной', 'A3', 250000, 25, bw_speed = 130, color_speed = 130)
b = Xerox('Cannon', 'CN2400', 'черно-белый', 'A3', 85000, 3, bw_speed = 60)
c = Scanner('Brother', 'ADS-1700W', 'цветной', 'A4', 31000, 5, scanner_type = 'протяжный')
my_store = Store()
my_store.get_tech(a.unit())
my_store.get_tech(b.unit())
my_store.send_item('XRS0')
print(my_store.xeroxes)
print()
print(Department.xeroxes)
print()
my_store.recover_item('XRS0')
print(my_store.xeroxes)
print()
print(Department.xeroxes)
my_store.get_tech(c.unit())
print(my_store.scanners)
