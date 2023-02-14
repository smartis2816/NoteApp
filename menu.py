import sys
import input
import funcs_csv as f_csv


def menu(input_menu):
    action = input_menu
    match action:
        case 'add':
            return f_csv.add_note(input.input_note())
        case 'show':
            return f_csv.show_all()
        case 'del':
            return f_csv.delete_note(input.find_head())
        case 'fd':
            return f_csv.find_date(input.input_date())
        case 'ch':
            return f_csv.change_note(input.find_head())
        case 'end':
            return sys.exit()
