import os


def check_or_make_folder(path):
    if os.path.exists(path):
        print(f'path alredy exists {path}')
    else:
        print(f'make folder {path}')
        os.mkdir(path)


def make_tree_folders(soucre_di):
    '''make folders from dict'''
    for key, value in soucre_di.items():
        check_or_make_folder(key)
        for i in value:
            path = os.path.join(key, i)
            check_or_make_folder(path)


if __name__ == '__main__':
    soucre_di = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
    make_tree_folders(soucre_di)
