from sys import argv


def run():
    with open(path_users_file) as users:
        gen_usr = (user.replace('\n', '') for user in users)

        with open(path_hobby_file) as hobbys:
            gen_hobby = (hobby.replace('\n', '') for hobby in hobbys)

            res_str = ''
            with open(path_result, 'w') as res:
                while True:
                    try:
                        res_str = f'{gen_usr.__next__()}: {gen_hobby.__next__()}\n'
                        res.write(res_str)
                    except StopIteration:
                        break


if len(argv) == 1:
    path_users_file = 'users.csv'
    path_hobby_file = 'hobby.csv'
    path_result = 'users_hobby.txt'
    run()
elif len(argv) != 4:
    print('''set names:
    1) users_names
    2) hobbys
    3) result_file ''')
elif len(argv) == 4:
    path_users_file = argv[1]
    path_hobby_file = argv[2]
    path_result = argv[3]
    run()
else:
    print('Not correct input')
