from person import *
import os


def main():
    person_list = PersonList()

    while True:
        print('-' * 30)
        print('1. Добавить человека', '\n2. Найти человека',
              '\n3. Удалить человека', '\n4. Сохранить',
              '\n5. Вывести базу', '\n6. Выйти', '\n7. Загрузить базу данных')
        print('-' * 30)
        choice = input('Выберите пункт меню: ')
        if choice == '1':

            while True:
                name = input('Введите имя: ')
                if name == '':
                    print('Имя не может быть пустым')
                else:
                    break
            surname = input('Введите фамилию: ')
            patronymic = input('Введите отчество: ')
            while True:
                sex = input('Введите пол (М/Ж): ').upper()
                if sex in ('М', 'Ж'):
                    break
                else:
                    print("Неправильный формат")
            while True:
                birthday = input('Введите дату рождения: ')
                try:
                    birthday = datetime.datetime.strptime(get_valid_date(birthday), '%d.%m.%Y').strftime('%d.%m.%Y')
                    break
                except ValueError:
                    print('Неверный формат даты')
            while True:
                data_death = input('Введите дату смерти: ')
                if len(data_death) == 0:
                    data_death = None
                    break
                else:
                    try:
                        data_death = datetime.datetime.strptime(get_valid_date(data_death), '%d.%m.%Y').strftime('%d.%m.%Y')
                        break
                    except ValueError:
                        print('Неверный формат даты')
            person_list.add_person(Person(name, surname, patronymic, sex, birthday, data_death))

        elif choice == '2':
            find = input('Введите слово по которому будет произведён поиск: ')
            person = person_list.find_persons(find)
            if person is not None:
                for i in person:
                    print(i)
            else:
                print('Человек не найден')
        elif choice == '3':
            if person_list.delete_person(input('Введите фамилию: ')):
                print('Человек удален')
            else:
                print('Человек не найден')
        elif choice == '4':
            if input('Сохранить в новый файл? (Да/Нет):').upper() in "ДА":
                file_name = input('Введите имя файла без расширения:')
                person_list.save(file_name)
            else:
                person_list.save(person_list.file_name)
        elif choice == '5':
            person_list.get_info()
        elif choice == '6':
            break
        elif choice == '7':
            file_name = input('Укажите имя файла:')
            if os.path.exists(f'{file_name}.xlsx'):
                person_list.load(file_name)
            else:
                print('Такого файла нет в корне')
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    main()
