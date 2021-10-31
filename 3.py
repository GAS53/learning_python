class My_exeption(ValueError):
    def __init__(self, *argv):
        self.message = argv[0]

    def __str__(self):
        return f'my error {self.message}'

    def check_digit(self, li):
        for num in li:
            try:
                print(f'{type(num)} num ')
                z = float(num)
            except ValueError:
                raise My_exeption

li = []
while True:
    in_value = input('введите значение для добавлени в список (q - для выхода) ')
    if in_value == 'stop':
        break
    try:
        try:
            val = float(in_value)
        except ValueError:
            raise My_exeption('введено некорректное значение')
    except My_exeption as e:
        print(f'my extption {e}')
    else:
        li.append(val)

print(f' result list {li}')
