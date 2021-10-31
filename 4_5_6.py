from abc import abstractmethod


class Store():
    def __init__(self):
        self.full_dict = {}

    def get_unit(self, unit, name):
        unit.set_id(name)
        self.full_dict[name] = unit


    def move_to_office(self, id):
        get_unit = self.full_dict.get(id)
        if get_unit:
            res = self.full_dict.pop(id)
            print(f'{res} move to office')
            return res
        else:
            print(f'NOT in store {id}')
            return None


    def check_store(self):
        print(f'all in store {len(self.full_dict)} units')
        if len(self.full_dict):
            print(f'this units is:')
            for name, cls in self.full_dict.items():
                print(name, cls)



class Office_equipment():
    @abstractmethod
    def __init__(self, in_name, in_type):
        self.name = in_name
        self.type_is = in_type

    def __str__(self):
        return f'{self.name} {self.type_is}'

    def to_print(self):
        print('need define')

    def get_name(self):
        print(f'{self.name} - {self.type_is}')


class Printer(Office_equipment):
    def __init__(self, name, type_is):
        super().__init__(name, type_is)

    @abstractmethod
    def to_do(self):
        print(f'{self.name} print pages')

    def __str__(self):
        return f'{self.name} {self.type_is}'


class Scaner(Office_equipment):
    def __init__(self, name, type_is):
        super().__init__(name, type_is)

    def to_scan(self):
        print(f'{self.name} scan to pages')


class MFU(Scaner, Printer):
    def __init__(self, name, type_is):
        Scaner.__init__(self, name, type_is)
        Printer.__init__(self, name, type_is)
        # self.id = prop

    def to_do(self):
        Scaner.to_scan(self)
        Printer.to_print(self)

    def get_inheritance(self):
        print(f'full inheritance clases:\n {MFU.__mro__}')

    @classmethod
    def get_info_class(cls):
        print(cls)

    @abstractmethod
    def check_info_mfu(cls):
        print(cls.__mro__)
        print(cls.__module__)
        print(cls.__dict__)

    @property
    def get_id(self):
        print(f'{self.name} have id {self.id}')

    def set_id(self, in_id):
        self.id = in_id


st = Store()  # создаем склад
st.check_store()  # проверяем склад

mfu = MFU('Xerox', 'R320')  # у нас есть  МФУ
MFU.get_info_class()  # проверяем класс
MFU.check_info_mfu(MFU)  # наследование, название модуля, информация о классе

st.get_unit(mfu, '1555')  # добавляем мфу на склад присваивая id идентификационный номер
st.check_store()

mfu = st.move_to_office('1555')  # склад передает МФУ в офис

mfu.to_do()  # тестируем МФУ это принтер и сканер одновременно
mfu.get_name()
mfu.to_scan()  # проверяем только сканирование
mfu.get_inheritance()  # проверяем наследование
print(mfu.get_id)  # проверяем id



mfu = st.move_to_office('1555') # пытаемся получить со склада такой-же МФУ
