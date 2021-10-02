def sorter(di):
    '''sort by keys'''
    sorted_keys = sorted(di)
    new_di = {}
    for key in sorted_keys:
        new_di[key] = di[key]
    return new_di


def thesaurus_adv(*args): # ...rus_adv(sort, *args): named args without unpack
    '''make dicts from string'''
    sort, *args = args
    di = {}
    for name_surname in args:
        name, surname = name_surname.split(' ')
        li_name_surname = [name_surname]
        if di.get(surname[0]) == None:
            iner_di = {}
        else:
            iner_di = di[surname[0]]
        if not iner_di.get(name[0]) == None:
            li_name_surname.extend(iner_di.get(name[0]))
        iner_di[name[0]] = li_name_surname
        if sort:
            iner_di = sorter(iner_di)
        di[surname[0]] = iner_di
    if sort:
        di = sorter(di)
    return di


di = thesaurus_adv(True, "Анна Савельева", "Иван Сергеев", "Инна Серова",
 "Петр Алексеев", "Илья Иванов", )
print(di)
