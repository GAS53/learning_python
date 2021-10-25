class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.bulk = 5  # задать толщину по умолчанию 5 см
        self.mass = 0.025  # задать массу в тоннах на 1 см толщины

    def calculation_1_meter(self):
        return self.bulk*self.mass

    def сalculation(self):
        '''calculation mass asphalt'''
        res = self._length * self._width * self.calculation_1_meter()
        return res


r = Road(5000, 20)
print(r.сalculation())
