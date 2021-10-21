li =  ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']






count=0
for i in li:
    if not i.isalpha():
        count+=3
    else:
        count+=1
len_update_li=count-len(li)
update_li=['' for _ in range(len_update_li)]
update_li.extend(li) # get len update li

li=update_li

def get_digit_str(num):
    for num1,i in enumerate(li[num:]):

        if i.isalpha() and not i=='':
            return True, i, num1
        elif not i.isalpha() and not i=='':
            return False, i, num1
not_count=0
for num, i in enumerate(li):
    if not_count<num:
        if i=='':
            check,return_i,ret_num=get_digit_str(num)
            if check:
                li[num]=return_i
                li[ret_num]=''
            else:
                li[num]='"'
                li[num+1]=return_i
                li[num+2]='"'
                not_count=num+2




# for num, i in enumerate(li):
#     # print(num,i)
#     if i=='':
#         print(f'i {num},{i}')
#         for num_j,j in enumerate(li):
#             print(f'j {num_j},{j}')
#             if j!='':
#                 print(j)
#                 if j.isalpha(): # нашелся текст
#                     li[num]=j
#                     li[num_j]=''
#                 else:  # нашлась цифра текст
#                     li[num]='"'
#                     li[num+1]=j
#                     li[num+2]='"'
#             break

print(li)
        # idex_fin=li.find('')
        # li[]


    # if i == '':
    #     for num_j,j in enumerate(li):
    #         if j!='':
    #             replace=li.pop(num_j)
    #             li.insert(num,replace)
    #             break



'''
count = 0
start = True
for val in li:
    if val == '"' and start:
        li.insert(count,f'{val} ')
        count+= 1
        start = False
    elif val == '"' and not start:
        li.insert(count,f' {val}')
        count+= 1
        start  =  True
    else:
        li.insert(count,val)
        count+= 1
res = ' '.join(li)
res = res.replace('  ','')
# print(f'res {res}')
# print(id(li))
'''
