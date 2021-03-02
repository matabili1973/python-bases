class ComplexNumber:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.left} + {self.right}i'

    def __add__(self, other):
        return f'({self.left + other.left}+{self.right + other.right}i)'

    def __sub__(self, other):
        return f'({self.left - other.left}-{abs(self.right - other.right)}i)'

    def __mul__(self, other):
        return f'({self.left * other.left - self.right * other.right}+{self.left * other.right + self.right * other.left}i)'


a = ComplexNumber(1, 0)
b = ComplexNumber(4, 12)
print(a * b)

