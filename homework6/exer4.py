class Car:
    speed = None
    color = None
    name = None
    is_police = False

    def __init__(self, speed, color, name):
        print('В городе появился новый автомобиль!')
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = Car.is_police

    def go(self):
        return 'Машина {} поехала!'.format(self_name)

    def stop(self):
        return 'Машина {} остановилась!'.format(self_name)

    def turn(self, direction):
        return 'Машина {} повернула {}!'.format(self_name, direction)

    def show_speed(self):
        return 'Скорость автомобиля {} составляет {} км/ч.'.format(self.name, self.speed)

class TownCar(Car):

    def show_speed(self):
        return 'Скорость автомобиля {} составляет {} км/ч.'.format(self.name, self.speed) + (' Скорость превышена!' * (self.speed > 60))

class WorkCar(Car):

    def show_speed(self):
        return 'Скорость автомобиля {} составляет {} км/ч.'.format(self.name, self.speed) + (' Скорость превышена!' * (self.speed > 40))

class SportCar(Car):

    def show_speed(self):
        return 'Автомобиль {} гоняет по городу со скоростью {} км/ч.'.format(self.name, self.speed)

class PoliceCar(Car):

    def __init__(self, speed, color, name):
        print('А вот и полиция присоединилась к общему веселью!')
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

    def show_speed(self):
        return 'Чтобы догнать нарушителя, надо ехать со скоростью {} км/ч.'.format(self.speed)

toyota_RAV4 = TownCar(80, 'black', 'Toyota RAV4')
mazda_CX5 = TownCar(50, 'red', 'Mazda CX5')
gazel = WorkCar(45, 'gray', 'Газель')
lotus_esprit = SportCar(90, 'blue', 'Lotus Esprit')
skoda_kodiaq = PoliceCar(91, 'white', 'Skoda Kodiaq vRS')

for counter in [toyota_RAV4, mazda_CX5, gazel, lotus_esprit, skoda_kodiaq]:
    print(counter.name, counter.color)
    print(counter.show_speed())
