class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return '{} {} {}'.format('Full name:', self.name, self.surname)

    def get_total_income(self):
        return '{} {}'.format('Total income:', self._income['wage'] + self._income['bonus'])

gendir = Position('Olga', 'Gromova', 'CEO', 120000, 40000)

print(gendir.get_full_name())
print(gendir.get_total_income())
