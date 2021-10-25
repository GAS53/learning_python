class Stationery():
    count_stationery = 0

    def __init__(self, title):
        Stationery.count_stationery += 1
        self.title = title

    def draw(self):
        print('start draw')


class Mod_Stationery(Stationery):  # чтобы не перегружать методы в каждом классе добавил мод
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'start draw by {self.title}')


class Pen(Mod_Stationery):
    def __init__(self):
        super().__init__('pen')

    def draw(self):
        print(f'PEN start draw by {self.title}')  # но можно и перегрузить в каждом классе как по заданию


class Pencil(Mod_Stationery):
    def __init__(self):
        super().__init__('pencil')


class Handle(Mod_Stationery):
    def __init__(self):
        super().__init__('handle')


pn = Pen()
pl = Pencil()
hl = Handle()

pn.draw()
pl.draw()
hl.draw()
