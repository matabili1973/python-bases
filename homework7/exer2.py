from abc import ABC, abstractmethod


class Clothes(ABC):
    
    @abstractmethod
    def calculation(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def calculation(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def calculation(self):
        return self.height * 2 + 0.3


mycoat = Coat(50)
mysuit = Suit(1.6)

print(round(mycoat.calculation + mysuit.calculation, 2))

