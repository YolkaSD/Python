import view


def add(data):
    with open('data_base.txt', 'a', encoding='utf-8') as file:
        file.write(data + '\n')


def search(desired):
    with open('data_base.txt', 'r', encoding='utf-8') as file:
        result = ''

        for line in file.readlines():
            if desired in line:
                result += line

        if result:
            return result
        else:
            return 'Нет совпадений!'


def sort(sort_type):
    if sort_type not in ['1', '2']:
        return 'Не ожидаемый ввод!'

    with open('data_base.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()

    if sort_type == '1':
        data.sort()
    elif sort_type == '2':
        data.sort(key=lambda x: (
            str(x).split('|')[2].split('.')[2],
            str(x).split('|')[2].split('.')[1],
            str(x).split('|')[2].split('.')[0]))

    with open('data_base.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)
    return data


def print_name():
    with open('data_base.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
        names = [line.split('|')[0] for line in data]
    i = 0
    return [f'{i + 1}. {name}\n' for i, name in enumerate(names, start=i)]


def refactor(number):
    with open('data_base.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    new_data = view.create_new_line()
    data[number - 1] = new_data + '\n'
    with open('data_base.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)


def remove(number):
    with open('data_base.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    data[number - 1] = ''
    with open('data_base.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)
