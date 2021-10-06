import requests
from decimal import Decimal
from time import gmtime, strftime
from sys import argv


def currency_rates(find_currency):
    '''решение через str'''
    req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if req.status_code == 200:  # check connection
        dat = req.headers
        li_date = dat['Date']
        res_date = strftime(li_date, gmtime())
        all_text = req.text
        lines = all_text.split('/Valute')
        for currency in lines:
            if '/ValCurs' in currency:
                return None
            char_code = cleaner(currency, 'CharCode')
            name = cleaner(currency, 'Name')
            value = cleaner(currency, 'Value')
            '''decimal создан специально для финансовых расчетов'''
            value = Decimal(value)
            if char_code == find_currency.upper():
                print(f'{char_code} один {name} стоит {value} рублей')
                return value, res_date
    else:
        print('bad connection')


def cleaner(currency, val):
    '''clean values'''
    try:
        val = currency.split(val)[1]
    except IndexError as e:
        # pass
        print(e)
    li = ['<', '>', '/']
    for i in li:
        val = val.replace(i, '')
    val = val.replace(',', '.')
    val = val.strip()
    return val


if __name__ == '__main__':
    if len(argv) > 1:
        res = currency_rates(argv[1])
        print(str(res))
    elif 2 < len(argv):
        for i in argv[1:]:
            res = currency_rates(argv[1])
            print(str(res))
