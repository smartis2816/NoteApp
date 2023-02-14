
def input_menu_csv():
    return input("""Список доступных команд.
    1) add - добавить заметку
    2) show - показать список заметок
    3) fd - найти заметку по дате добавления
    4) ed - редактировать заметку
    5) del - удалить заметку
    6) end - завершить программу
    """)

def input_note():
    head = input('Введите заголовок: ')
    body = input('Введите текст заметки: ')
    info = head + ' ' + body
    return info

def input_head():
    return input('Введите заголовок заметки для поиска: ')

def input_date():
    return input('Введите дату в формате гг мм дд: ')