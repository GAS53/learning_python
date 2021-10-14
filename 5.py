from sys import argv
import csv

path_db = 'bakery.csv'


def print_db():
    '''show all db'''


def add_in_db(inner):
    '''add in db'''
    with open(path_db, 'a') as file:
        csv.writer(file, inner)

if len(argv) == 1:
    print_db()
elif len(argv) ==2:
    add_in_db(argv[1])
