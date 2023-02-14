import input
import funcs_csv as f_csv

def menu_csv(input_menu):
    choice = input_menu
    match choice:
        case 'add':
            return f_csv.add_note(input.input_note())
        case 'show':
            return f_csv.show_all()
        case 'del':
            return f_csv.delete_note(input.input_head())
        case 'fd':
            return f_csv.find_date(input.input_date())
        case 'ed':
            return f_csv.edit_note(input.input_head())
        case 'exit':
            return -1

