class Date():
    def __init__(self, inner_date):
        print('innit metod is work')
        self.date = inner_date

    @classmethod
    def func_class_extract(cls, date):
        print('class metod is work')
        return list(int(i) for i in date.split('-'))

    @staticmethod
    def func_validator(inner):
        print('static metod is work')
        if 0 < inner[0] < 31:
            print(f'day  {inner[0]} ok')
        else:
            print(f'error day {inner[0]}')
        if 0 < inner[1] < 13:
            print(f'month {inner[1]} ok')
        else:
            print(f'error month {inner[0]}')
        if 2000 < inner[2] < 2022:
            print(f'year {inner[1]} ok and period 2000-2022')
        else:
            print(f'error year {inner[0]}')


Date('12-10-2021')  # innit metod is work

res = Date.func_class_extract('12-10-2021')  # class metod is work
print(res)

Date.func_validator(res)  # static metod is work
