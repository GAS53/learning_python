class Cage():
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'{Cage} quantity -  {self.quantity}'

    def __add__(self, new):
        new_quantity = self.quantity + new.quantity
        return Cage(new_quantity)

    def __sub__(self, new):
        res = self.quantity - new.quantity
        if res > 0:
            return res
        else:
            print('error pirnt!!!!!!!!')

    def __mul__(self, new):
        new_quantity = self.quantity * new.quantity
        return Cage(new_quantity)

    def __truediv__(self, new):
        new_quantity = int(self.quantity / new.quantity)
        return Cage(new_quantity)

    def make_order(self, value):
        count = 0
        res = ''
        for i in range(self.quantity):
            res += '*'
            count += 1
            if count == value:
                res += '\n'
                count = 0
        return res


c1 = Cage(10)
c2 = Cage(2)

c3 = c1 / c2
# print(c3)
c4 = Cage(20)
res = c4.make_order(5)
print(res)
