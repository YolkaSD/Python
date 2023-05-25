def user_input():
    return input(
        'Выбери ниже '
        '\n1 - записать пользователя в телефонную книгу'
        '\n2 - поиск'
        '\n3 - сортировка'
        '\n4 - вывод имен'
        '\n5 - изменить'
        '\n6 - удалить'
        '\n7 - выйти'
        '\n')


def create_new_line():
    full_name = input('Введите ФИО: ').strip()
    phone_number = input('Введите номер телефона: ').strip()
    birthday = input('Введите дату рождения: ').strip()
    return f'{full_name}|{phone_number}|{birthday}|'


def sort():
    return input('Сортировка \n1 - по имени\n2 - по дате рождения\n')
