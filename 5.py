#'5. Создать список, содержащий цены на товары (10–20 товаров), например: [57.8, 46.51, 97, ...]


from random import randint
li_price = [f'{randint(10, 99)}.{randint(0, 100)}' for _ in range(20)]



# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
new_li_price=[]
for i in li_price:
    rub,cop=i.split('.')
    if len(cop) == 1: # как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
        cop= f'0'+cop
    elif len(cop) == 0:
        cop='00'
    price=f'{rub} руб {cop} коп'
    new_li_price.append(price)
print(new_li_price) # цена должна отображаться в виде <r> руб <kk> коп

#Подумать, как из цены получить рубли и копейки

for i in new_li_price:
    i=i.split(' ')
    rub=i[0] # get rub
    cop= i[2]  # get cop

print(new_li_price)
new_li_price.sort()
print(new_li_price) # Вывести цены, отсортированные по возрастанию

print(str(id(new_li_price))+' '+str(id(new_li_price))) # доказать, что объект списка после сортировки остался тот же

# Создать новый список, содержащий те же цены, но отсортированные по убыванию
new_li_price2=new_li_price.copy()
new_li_price2.sort(reverse=True) # то же самое возможно [::-1] или .reverse()
print(new_li_price2) # revers sort

# Вывести цены пяти самых дорогих товаров.
five_high_price=new_li_price2[:5]
print(five_high_price)

#Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print(sorted(five_high_price)) #
