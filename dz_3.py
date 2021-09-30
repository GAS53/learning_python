'''Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой
для каждого из чисел в интервале от 1 до 100'''


def get_procent(num):
    li_except=[11,12,13,14]
    if num in li_except:
        return 'процентов'
    else:
        num=str(num)
        digit=int(num[-1])
        if 1 == digit:
            return 'процент'
        if 1<digit<5:
            return 'процента'
        elif 4<digit or digit == 0:
            return 'процентов'


for digit in range(1,101):
    proc=get_procent(digit)
    print(f'{digit} {proc}')
