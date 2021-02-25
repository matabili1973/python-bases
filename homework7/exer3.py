class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return Cell(self.quantity - other.quantity)
        else:
            print('The difference between two cells is equal to {}'.format(self.quantity - other.quantity))

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(round(self.quantity / other.quantity))

    def make_order(self, inrow):
        string = ''
        for counter in range(self.quantity // inrow):
            string += ('*' * inrow + '\n')
        string += ('*' * (self.quantity % inrow))
        return(string)

    def __str__(self):
        return 'Количество ячеек в результирующей клетке равно {}'.format(self.quantity)


mycell1 = Cell(25)
mycell2 = Cell(16)

print(mycell1 + mycell2, mycell1 - mycell2, mycell1 * mycell2, mycell1 / mycell2, sep = '\n')
newcell = mycell1 + mycell2
print(newcell.make_order(8))
