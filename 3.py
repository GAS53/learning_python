from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

tutor_gen = zip_longest(tutors, klasses, fillvalue=None)
print(next(tutor_gen))  # test

'''сделал чтобы в tutors было больше элементов чтобы подходить под задание'''
a = ['Станислав', 'Вячеслав', 'Игорь']
tutors.extend(a)

tutor_gen2 = zip_longest(tutors, klasses, fillvalue=None)
for i in range(len(tutors)+1):  # test2
    print(next(tutor_gen2))
