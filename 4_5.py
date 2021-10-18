import os
from os import stat
import json


di_sizes = {100: (0, []), 1000:  (0, []), 10000:  (0, []), 100000:  (0, [])}
dir_path = '/run/user/1000/gvfs/smb-share:server=keenetic-2254.local,share=server/Project/GeekBrains/homework/7/some_data'


def get_info_file(size):
    '''get file stats'''
    count, tp = di_sizes[size]
    count += 1
    tp.append(path.split('.')[-1])
    tp = list(set(tp))
    di_sizes[size] = (count, tp)


files = os.listdir(dir_path)
for file in files:
    path = os.path.join(dir_path, file)
    if 0 < stat(path).st_size < 100:
        get_info_file(100)
    elif 100 < stat(path).st_size < 1000:
        get_info_file(1000)
    elif 1000 < stat(path).st_size < 10000:
        get_info_file(10000)
    elif 10000 < stat(path).st_size < 100000:
        get_info_file(100000)

print(di_sizes)
with open('summary.json', 'w') as file:
    json.dump(di_sizes, file)
