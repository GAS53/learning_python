from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeat=False):
    '''make jokes'''
    result_li = []
    li_nouns = []
    li_adverbs = []
    li_adjectives = []
    li_nouns = check_repeat(repeat, nouns, n)
    li_adverbs = check_repeat(repeat, adverbs, n)
    li_adjectives = check_repeat(repeat, adjectives, n)
    for a, b, c in zip(li_nouns, li_adverbs, li_adjectives):
        result_li.append(f'{a} {b} {c}')
    print(result_li)


def check_repeat(repeat, li, length):
    '''check for repeats'''
    count = 0
    new_li = []
    while count < length:
        a = choice(li)
        if not repeat:
            if a in new_li:
                continue
            else:
                new_li.append(a)
        else:
            new_li.append(a)
        count += 1
    return new_li


get_jokes(2)
