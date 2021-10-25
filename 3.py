
class Worker():
    income = {'wage': 100, 'bonus': 20}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        res = self.income['wage']*self.income['bonus']
        print(f' full income {res}')


pos = Position('Виктор', 'Петров', 'Програмист')
pos.get_full_name()
pos.get_total_income()
print(pos.income)
