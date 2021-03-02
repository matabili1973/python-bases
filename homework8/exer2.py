class MyError(Exception):

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def divide_by_zero(self):
        try:
            return (self.number1 / self.number2)
        except:
            return 'Делить на ноль нельзя!'


number1, number2 = float(input()), float(input())
myclass = MyError(number1, number2)
print(myclass.divide_by_zero())

