def thesaurus(*args):
    di = {}
    for name in args:
        if di.get(name[0]) != None:
            di[name[0]].append(name)
        else:
            new_li = []
            new_li.append(name)
            di[name[0]] = new_li
    return di


di = thesaurus("Петр", "Иван", "Мария", "Илья")
print(di)
'''полезен ли будет вам оператор распаковки? - да'''

# Как поступить, если потребуется сортировка по ключам?
sorted_keys = sorted(di)
new_di = {}
for key in sorted_keys:
    new_di[key] = di[key]

'''или генератором словарей'''
new_di = {key: di[key] for key in sorted(di)}
print(new_di)
