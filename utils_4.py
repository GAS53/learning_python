from dz_2_3 import currency_rates


def find_currency_cost():
    '''call currency_rates 3 times'''
    li_currency = ['eur', 'USD', "GBp"]  # check register
    for currency in li_currency:
        currency_rates(currency)


if __name__ == '__main__':
    find_currency_cost()
