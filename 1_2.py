
def odd_nums(num):
    '''get odd numbers'''
    for res in range(1, num+1, 2):
        yield res


num = 15
odd_to_15 = odd_nums(num)

print(next(odd_to_15))


odd_to_15 = (x for x in range(1, num+1, 2))
