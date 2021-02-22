class Road:

    def __init__(self, length, width, weight, depth):
        self._length = length
        self._width = width
        self._weight = weight
        self._depth = depth

    def get_weight(self):
        return self._length * self._width * self._weight * self._depth / 1000

my_road1 = Road(20, 5000, 25, 5)
print('Полная масса асфальта для дороги: {} тонн'.format(my_road1.get_weight()))
