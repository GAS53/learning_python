import re
from collections import Counter


def find_spammer(li, how_many_spamers=2):
    '''найти спамера/ов'''
    # print(li)
    ip_list = (s[0] for s in li)
    di_res = Counter(ip_list)
    print(di_res.most_common(how_many_spamers))


def get_pars_logs():
    '''обработчик лог файла'''
    result_li = []
    with open('nginx_logs.txt', 'r') as file:
        for line in file:
            pat = r'^\d+.\d+.\d+.\d+'
            pat_call = r'GET \s*\S*'
            try:
                ip = re.search(pattern=pat, string=line)[0]
                call = re.search(pat_call, string=line)[0]
                get, load = call.split(' ')
                tup = ip, get, load
                result_li.append(tup)
            except TypeError:
                pass
            line = file.readline()
    find_spammer(result_li)


get_pars_logs()
