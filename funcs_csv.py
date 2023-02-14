import csv
import os
from datetime import datetime

import input

path_csv = r'note_app.csv'


def add_note(info):
    new_list = info.split(',')
    now = datetime.now().strftime('%Y %m %d %H %M %S')
    with open(path_csv, 'a', encoding='utf-8') as data:
        file_writer = csv.writer(data, delimiter=";", lineterminator="\r")
        file_writer.writerow([now, new_list[0], new_list[1]])


def show_all():
    if os.path.getsize(path_csv) == 0:
        print('Заметок ещё нет')
    with open(path_csv, 'r', encoding='utf-8') as data:
        file_reader = csv.reader(data, delimiter=";", lineterminator="\r")
        num = 1
        for row in file_reader:
            print(str(num) + ')', '{:<20} {:<20} {:<20}'.format(*row))
            num += 1


def find_date(date):
    with open(path_csv, 'r', encoding='utf-8') as data:
        file_reader = csv.reader(data, delimiter=";", lineterminator="\r")
        num = 1
        for row in file_reader:
            if date in row[0]:
                print(str(num) + ')', '{:<20} {:<20} {:<20}'.format(*row))
                num += 1
        if num == 1:
            print('Заметок с выбранной датой не обнаружено')


def delete_note(name):
    new_list = []
    count = 0
    with open(path_csv, 'r', encoding='utf-8') as data:
        file_reader = csv.reader(data, delimiter=";", lineterminator="\r")
        for row in file_reader:
            new_list.append(row)
    for item in new_list:
        if name in item:
            new_list.remove(item)
            count += 1
    if count == 0:
        print('Заметок с таким заголовком не оказалось')
        return -1
    else:
        with open(path_csv, 'w', encoding='utf-8') as data:
            file_writer = csv.writer(data, delimiter=";", lineterminator="\r")
            file_writer.writerows(new_list)


def change_note(name):
    if delete_note(name) == -1:
        return
    else:
        add_note(input.input_change_note())
