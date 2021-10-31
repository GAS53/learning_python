class Complex_digit():
    def __init__(self, in_digit):
        self.digit = in_digit

    def check_negativ(self, digit):
        return -int(digit) if digit.startswith('-') else int(digit)

    def preparation(self, digit):
        digit = digit.replace('i', '')
        if digit.startswith('-'):
            digit = digit[1:]
            if '-' in digit:
                a, b = digit.split('-')
                return -int(a), -int(b)
            else:
                a, b = digit.split('+')
                return -int(a), int(b)
        else:
            if '-' in digit:
                a, b = digit.split('-')
                return int(a), -int(b)
            else:
                a, b = digit.split('+')
                return int(a), int(b)

    def un_preparation(self, tup):
        mark = '+' if tup[1] > 0 else ''
        return f'{tup[0]}{mark}{tup[1]}i'

    def __add__(self, two):
        a, b = self.preparation(self.digit)
        c, d = self.preparation(two.digit)

        aa = a+c
        bb = b+d

        res = self.un_preparation((aa, bb))
        print(res)
        return Complex_digit(res)

    def __mul__(self, two):
        a, b = self.preparation(self.digit)
        c, d = self.preparation(two.digit)

        aa = a*c-b*d
        bb = a*d+b*c

        res = self.un_preparation((aa, bb))
        print(res)
        return Complex_digit(res)

#
a = Complex_digit('5-6i')
b = Complex_digit('-3+2i')
c = a + b
# print(c)
a = Complex_digit('1+3i')
b = Complex_digit('4-2i')
c = a * b
# print(c)
a = Complex_digit('3-2i')
b = Complex_digit('4+1i')
c = a * b
print(c)


import cmath  # для работы с комплексными числами
