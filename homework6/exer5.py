class Stationary():
    title = None

    def draw(self):
        return 'Запуск отрисовки'

class Pen(Stationary):
    title = 'Ручка'

    def draw(self):
        return 'Начат процесс письма ручкой'

class Pencil(Stationary):
    title = 'Карандаш'

    def draw(self):
        return 'Начат процесс отрисовки карандашом'

class Marker(Stationary):
    title = 'Маркер'

    def draw(self):
        return 'Начат процесс отрисовки маркером'

a = Pen()
b = Pencil()
c = Marker()

for counter in [a, b, c]:
    print(counter.draw())

