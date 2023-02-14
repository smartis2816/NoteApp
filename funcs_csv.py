import csv
import os
import input
from datetime import datetime
from pathlib import Path

path_csv = r'note_app.csv'


# def csv_is_exist():
#     if not os.path.exists('/note_app.csv'):
#         Path('note_app.csv').touch()


def csv_check():
    if os.path.getsize(path_csv) == 0:
        with open(path_csv, 'a', encoding='utf-8') as data:
            file_writer = csv.writer(data, delimiter=";", lineterminator="\r")
            file_writer.writerow(["Дата", "Заголовок", "Текст"])
    else:
        return


def add_note(info):
    new_list = info.split()
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

def delete_note(name):
    new_list = []
    with open(path_csv, 'r', encoding='utf-8') as data:
        file_reader = csv.reader(data, delimiter=";", lineterminator="\r")
        for row in file_reader:
            new_list.append(row)
    for item in new_list:
        if name in item:
            new_list.remove(item)
    with open(path_csv, 'w', encoding='utf-8') as data:
        file_writer = csv.writer(data, delimiter=";", lineterminator="\r")
        file_writer.writerows(new_list)

def edit_note(name):
    return