

class ZeroDiv(ZeroDivisionError):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return f'my zero division {self.message}'
        else:
            return f'my zero division'

# raise ZeroDiv

# one_in = int(input('введите значение делимого '))
def test_func():
    one_value = 5
    two_value = 0

    try:
        one = float(one_value)
        two = float(two_value)
        res = one/two
    except ValueError:
        print(f'некорректно введено значение')
    except ZeroDivisionError as e:
        print('перехват базового ZeroDivisionError')
        raise ZeroDiv('test_zero_div')


if __name__ == '__main__':
    try:
        test_func()
    except ZeroDiv:
        print('перехват моего ZeroDiv')
        print('ok')
