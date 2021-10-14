from sys import argv

path_db = 'bakery.csv'


def print_db():
    '''show all db'''
    with open(path_db, 'r') as file:
        db = file.read()
        print(db, end='')


def add_in_db(inner):
    '''add in db'''

    with open(path_db, 'a') as file:
        inner = inner.replace('\n', '')
        file.write(f'{inner}\n\r')


def print_period(start, stop):
    bool_start = False
    with open(path_db, 'r') as file:
        for num, line in enumerate(file.readlines()):
            if bool_start:
                print(line, end='')
            if str(num) == start:
                bool_start = True
            elif stop == str(num):
                break


if len(argv) == 1:
    print_db()
elif len(argv) ==2:
    add_in_db(argv[1])
elif len(argv) ==3:
    print_period(argv[1], argv[2])
