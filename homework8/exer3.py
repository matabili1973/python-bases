class IsNumber:

    def __init__(self, string):
        self.string = string

    def check_number(self):
        try:
            return float(self.string)
        except:
            print(f'{self.string} - не число!')


mylist = []
while True:
    mystring = input()
    if mystring == 'stop':
        break
    myclass = IsNumber(mystring)
    if myclass.check_number() != None:
        mylist.append(myclass.check_number())
print(mylist)
