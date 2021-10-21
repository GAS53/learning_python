from functools import wraps


def type_logger(func):

    @wraps(func)
    def wrap_func(*args):
        new_li = []
        z = func(*args)
        for i in z:
            new_li.append((i, type(i)))
        return new_li
    return wrap_func


@type_logger
def calc_cube(*args):
    '''get args in cube'''
    li = []
    if type(args) == list or type(args) == tuple:
        for a in args:
            li.append(int(a)**3)
    else:
        li = int(args)**3
    return li


a = calc_cube(5, 54, 3)
print(a)
