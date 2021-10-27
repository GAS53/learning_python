from abc import abstractmethod

class Clothes():
    def __init__(self, name, param):
        self.name = name
        self.param = param

    def __str__(self):
        return f'{self.name} size {self.param}'

    @abstractmethod
    def rate_textile(self):
        self.all_textile = 2*self.param + 0.3
        return self.all_textile

    def __add__(self, Clothes):
        return self.all_textile + Clothes.all_textile



class Coat(Clothes):
    # def __init__(self, name, param):
        # super().__init__(f'   zzzz {name}', param)
        # Clothes.name = f'   zzzz {name}'
        # Clothes.param = param
    @property
    def rate_textile(self):
        self.all_textile = self.param/6.5 + 0.5
        return self.all_textile




class Suit(Clothes):
    @property
    def rate_textile(self):
        self.all_textile = 2*self.param + 0.3
        return self.all_textile








co = Coat('пальто', 44)
su = Suit('костюм', 42)
print(co.rate_textile)  # test property
print(su.rate_textile)  # test property

all = co + su
print(all)
