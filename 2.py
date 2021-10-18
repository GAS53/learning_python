import os


def check_or_make_folder(path, is_file=False):
    if os.path.exists(path):
        print(f'path alredy exists {path}')
    else:
        print(f'make new folder {path}')
        if is_file:
            with open(os.path.join(path), 'w') as file:
                file.write(' ')
        else:
            os.mkdir(path)


def make_tree_folders(source, path=False):
    '''make folders from dict'''
    if type(source) == str:
        # print(f' in str block {source}, {type(source)}')
        check_or_make_folder(os.path.join(path, source), is_file=True)
    elif type(source) == list:
        # print(f' in list block {source}, {type(source)}')
        for i in source:
            # print(i, type(i), path)
            make_tree_folders(i, path)
    elif type(source) == dict:
        # print(f' in dict block {source}, {type(source)}')
        for k, v in source.items():
            new_path = os.path.join(path, k) if path else k
            check_or_make_folder(new_path)
            make_tree_folders(v, new_path)
    else:
        print(f'not correct value {source} type {type(source)}')


if __name__ == '__main__':
    soucre_di = {
    'my_project': [
    {'settings': ['__init__.py', 'dev.py', 'prod.py']},
    {'mainapp': [' __init__.py', 'models.py', 'views.py', {'templates': {'mainapp': ['base.html', 'index.html']}}]},
    {'authapp': ['__init__.py', 'models.py', 'views.py', {'templates': {'authapp': ['base.html', 'index.html']}}]}
    ]}
    make_tree_folders(soucre_di)
