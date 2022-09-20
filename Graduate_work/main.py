from person import *
# Импортируем наш модуль для работы с данными и файлами 'person.py'
import os
# Импортируем модуль для для проверки существования файла


def main():
    person_list = PersonList()
    # Создаем обьект* "список людей" из класса PersonList
    while True:
        print('-' * 30)
        print('1. Загрузить базу данных''\n2. Добавить человека', '\n3. Найти человека',
              '\n4. Удалить человека', '\n5. Сохранить',
              '\n6. Вывести базу', '\n7. Выйти')
        print('-' * 30)
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            file_name = input('Укажите имя файла: ')
            if os.path.exists(f'{file_name}.xlsx'):
                person_list.load(file_name)
            else:
                print('Такого файла нет в корне')
            # Загружаем базу данных из файла, если такой есть. Если нет, то выводим
            # сообщение об ошибке и возвращаемся в меню
        elif choice == '2':

            while True:
                name = input('Введите имя: ').title()
                if name == '':
                    print('Имя не может быть пустым')
                else:
                    break
            while True:
                surname = input('Введите фамилию: ').title()
                if surname == '':
                    print('Фамилия не может быть пустая')
                else:
                    break
                # Сделали проверку фамилии ради того чтобы можно было корректно удалять людей
            patronymic = input('Введите отчество: ').title()
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
            # Добавляем человека, просим ввести данные
        elif choice == '3':
            find = input('Введите слово по которому будет произведён поиск: ')
            person = person_list.find_persons(find)
            if person is not None:
                for i in person:
                    print(i)
            else:
                print('Человек не найден')
            # Делаем запрос на поиск человека по имени, фамилии или отчеству. Если человек или люди найдены, то
            # выводим их на экран и возвращаемся в меню
        elif choice == '4':
            if person_list.delete_person(input('Введите фамилию: ')):
                print('Человек удален')
            else:
                print('Человек не найден')
            # Удаляем по фамилии ибо фамилии повторяются намного реже чем имена. дабы не
            # удалять всех с одинаковыми именами
        elif choice == '5':
            if input('Сохранить в новый файл? (Да/Нет): ').upper() in "ДА":
                file_name = input('Введите имя файла без расширения:')
                person_list.save(file_name)
            elif person_list.file_name is not None:
                person_list.save(person_list.file_name)
            else:
                print('Файл не выбран')
            # Если пользователь сохраняет в новый файл, просим написать название файла. Если пользователь сохраняет в
            # старый файл то проверяем есть ли у нас имя файла в корне и если есть то сохраняем в него, а если нет, то
            # выводим что такого файла нету
        elif choice == '6':
            person_list.get_info()
            # Принтим нашу базу
        elif choice == '7':
            break
            # Выходим из программы (выход из цикла)
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    main()
# Проверяем что мы запускаем не модуль, а саму программу и если да, то запускаем функцию main)
# Все функции и методы имеют комментарии
# --------#
# The End #
# ------------------------------------------------------------------------------#
# Программа была написана такими студентами: ('Даниил Чупак', 'Андрей Верыч') ^)
# ------------------------------------------------------------------------------#

# Спасибо за внимание!
