from di_for_1_and_2 import di
'''2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
реализовать корректную работу с числительными, начинающимися с заглавной буквы
— результат тоже должен быть с заглавной.'''


def num_translate_adv(num):
    if num[0].istitle():
        print(di[num.lower()].capitalize())
    else:
        print(di[num])


num_translate_adv('Two')
num_translate_adv('two')
