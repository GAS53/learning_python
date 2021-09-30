'''точное выполнение задания'''
duration  =  400153
if duration < 60:
    print(f'{duration} сек ')
elif 60  <  duration  <  3600:
    minute  =  duration // 60
    # duration = duration//60
    sec  =  duration % 60
    print(f'{minute} мин {sec} сек')
elif 3600 < duration < 86400:
    hour = duration//3600
    duration = duration%3600
    minute = duration//60
    sec = duration%60
    print(f'{hour} час {minute} мин {sec} сек')
elif 86400 < duration:
    day = duration//86400
    duration = duration%86400
    hour = duration//3600
    duration = duration%3600
    minute = duration//60
    sec = duration%60
    print(f'{day} дн {hour} час {minute} мин {sec} сек')







'''модернизированная версия
 названия всех констант большими буквами sec - SEC
 и они должны быть импортированы из отдельного файла:
  from const import SEC
русского в коде быть не должно
'''

sec = 1
minute = sec*60
hour = minute*60
day = hour*24


def get_time(full_time):
    '''get periods from seconds'''
    result = ''
    days = full_time//day
    if days:
        result += f'{days} дн '
    full_time = full_time%day
    hours = full_time//hour
    if hours:
        result += f'{hours} час '
    full_time = full_time%hour
    minutes = full_time//minute
    if minutes:
        result += f'{minutes} мин '
    full_time = full_time%minute
    seconds = full_time
    if seconds:
        result += f'{seconds} сек '
    print(result)


get_time(400153)

'''подумайте, можно ли использовать цикл для проверки работы кода
сразу для нескольких значений продолжительности, будет ли тут полезен список?'''

'''ответ: проверить можно с помощью любого цикла, удобно- for неудобно- while
Пример'''

li_seconds = [53,153,4153,400153]
for second in li_seconds:
    get_time(second)
