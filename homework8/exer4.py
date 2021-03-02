class Store:
    pass


class Tech:
    
    def __init__(self, device, manufactor, model, price, quantity):
        self.device = device
        self.manufactor = manufactor
        self.model = model
        self.price = price
        self.quantity = quantity


class Printer(Tech):
    
    def __init__(self, *args, technology = 'не указана', color = 'не указана'):
        self.technology = technology
        self.color = color
        super().__init__('Принтер', *args)

    def __str__(self):
        return f'{self.device} {self.manufactor} {self.model}, цена: {self.price}руб., количество: {self.quantity} шт.'

    def unit(self):
        return {
            'Тип устройства': self.device,
            'Изготовитель': self.manufactor,
            'Модель': self.model,
            'Технология печати': self.technology,
            'Цветность печати': self.color,
            'Розничная цена': self.price,
            'Количество': self.quantity
            }


class Scanner(Tech):

    def __init__(self, *args, scanner = 'не указан'):
        self.scanner = scanner
        super().__init__('Сканер', *args)

    def __str__(self):
        return f'{self.device} {self.manufactor} {self.model}, цена: {self.price}руб., количество: {self.quantity} шт.'

    def unit(self):
        return {
            'Тип устройства': self.device,
            'Тип сканера': self.scanner,
            'Изготовитель': self.manufactor,
            'Модель': self.model,
            'Розничная цена': self.price,
            'Количество': self.quantity
            }


class Xerox(Tech):

    def __init__(self, *args, speed):
        self.speed = speed
        super().__init__('Копир', *args)

    def __str__(self):
        return f'{self.device} {self.manufactor} {self.model}, цена: {self.price}руб., количество: {self.quantity} шт.'

    def unit(self):
        return {
            'Тип устройства': self.device,
            'Изготовитель': self.manufactor,
            'Модель': self.model,
            'Скорость копирования, страниц в минуту': self.speed,
            'Розничная цена': self.price,
            'Количество': self.quantity
            }


a = Printer('Hewlett-Packard', 'LaserJet 1020', 18000, 25, technology = 'струйная', color = 'цветная')
b = Xerox('Ricoh', 'DD 3344', 265000, 10, speed = 130)
print(a, a.unit(), sep = '\n')
print(b, b.unit(), sep = '\n')
