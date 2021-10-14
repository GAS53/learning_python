from sys import argv

path_db = 'bakery.csv'


def set_new(num, value):
    count = 1
    with open(path_db, 'r+') as file:
        line = file.readline()
        while line:
            if str(count) == num:
                pos = file.tell()
                file.seek(pos)
                file.write(value)
                break
            line = file.readline()
            count += 1
        else:
            print(f'file not have position {num}')


if len(argv) == 3:
    set_new(argv[1], argv[2])
