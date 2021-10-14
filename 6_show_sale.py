from sys import argv

path_db = 'bakery.csv'


def print_db():
    '''show all db'''
    with open(path_db, 'r') as file:
        line = file.readline()
        while line:
            print(line, end='')
            line = file.readline()


def print_period(start, stop=None):
    bool_start = False
    count = 1
    with open(path_db, 'r') as file:
        line = file.readline()
        while line:
            if str(count) == start:
                bool_start = True
            elif stop == str(count):
                print(line, end='')
                break
            if bool_start:
                print(line, end='')
            line = file.readline()
            count += 1


if len(argv) == 1:
    print_db()
elif len(argv) == 2:
    print_period(argv[1])
elif len(argv) == 3:
    print_period(argv[1], argv[2])
