import re


def email_parse(email):
    if '@' not in email:
        raise ValueError('email don`t have - @')
    elif '.' not in email:
        raise ValueError('email don`t have - .')
    di = {}
    all = re.findall(r'[a-zA-Z1-9]*', email)
    di['username'] = all[0]
    di['domain'] = all[2]
    print(di)


email = 'someone@geekbrains.ru'
email_parse(email)
