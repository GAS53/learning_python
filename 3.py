
with open('users.csv') as file:
    names = file.readlines()

with open('hobby.csv') as file:
        hobby = file.read().split(',')
len_names = len(names)
len_hobby = len(hobby)
while len_hobby < len_names:
    hobby.append('None')
    len_hobby = len(hobby)
if len_names < len_hobby:
    exit(1)

new_di = {}
for i, name in enumerate(names):
    new_di[name.replace('\n', '')] = hobby[i].replace('\n', '')
print(new_di)

with open('result.txt', 'w') as file:
    for k, v in new_di.items():
        line = f'{k} {v}\n'
        file.write(line)
