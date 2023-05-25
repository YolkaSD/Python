import view
import databasse


def main():
    while True:
        ask = view.user_input()
        if ask == '1':
            databasse.add(view.create_new_line())
        elif ask == '2':
            print(databasse.search(input('Введите строку поиска: ')))
        elif ask == '3':
            print(*databasse.sort(view.sort()))
        elif ask == '4':
            print(*databasse.print_name())
        elif ask == '5':
            print(*databasse.print_name())
            databasse.refactor(int(input('Введите номер изменения: ')))
        elif ask == '6':
            databasse.remove(int(input('Введите номер удаления: ')))
        elif ask == '7':
            break


main()
