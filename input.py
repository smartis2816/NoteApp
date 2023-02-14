def input_menu():
    return input("""Список доступных команд.
    1) add - добавить заметку
    2) show - показать список заметок
    3) fd - найти заметку по дате добавления
    4) ch - перезаписать заметку
    5) del - удалить заметку
    6) end - завершить программу
    """)


def input_note():
    head = input('Введите заголовок: ')
    body = input('Введите текст заметки: ')
    info = head + ',' + body
    return info

def input_change_note():
    head = input('Введите новый заголовок: ')
    body = input('Введите новый текст заметки: ')
    info = head + ',' + body
    return info


def find_head():
    return input('Введите заголовок заметки, которую надо найти: ')


def input_date():
    return input('Введите дату в формате гг мм дд: ')
