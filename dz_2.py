

'''Создать список, состоящий из кубов нечётных чисел от 1 до 1000'''
li_cube=[]
for num in range(1000):
    if num % 2 != 0:
        li_cube.append(num**3)


li_cube=[x ** 3 for x in range(1000) if not x % 2 == 0] # создание генератором

'''a Вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7'''

def get_devide_seven(li):
    new_summ_list=[]
    for num in li:
        new_summ=0
        for digit in str(num):
            new_summ+=int(digit)
        if new_summ % 7 == 0:
            new_summ_list.append(new_summ)

    result=0
    for digit in new_summ_list:
        result+=digit
    print(result)
    return result

get_devide_seven(li_cube)


'''b К каждому элементу списка добавить 17 и
заново вычислить сумму тех чисел из этого списка,
 сумма цифр которых делится нацело на 7'''

new_li_17=[]
for i in li_cube:
    new_li_17.append(i+17)

get_devide_seven(new_li_17)

'''* Решить задачу под пунктом b, не создавая новый список'''
new_li_cube=[x ** 3+17 for x in range(1000) if not x % 2 == 0]
get_devide_seven(new_li_cube)
