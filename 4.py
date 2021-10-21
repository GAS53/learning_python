from functools import wraps


def val_checker(func):

    @wraps(func)
    def wrap_args(*args):
        check_argv = args
        for i in check_argv:
            if i < 0:
                raise ValueError('Error - value less zero')
        res = func(check_argv)
        return res
    return wrap_args


@val_checker
def calc_cube(*args):
    '''get args in cube'''
    li = []
    if type(args) == list or type(args) == tuple:
        for a in args:
            li.append(int(a)**3)
    else:
        li = int(args)**3
    return li


res = calc_cube(1, -3, 4)
print(res)
