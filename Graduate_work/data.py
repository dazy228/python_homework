import datetime

while True:
    birthday = input('Введите дату рождения: ')
    try:
        birthday = datetime.datetime.strptime(birthday, '%d.%m.%Y').strftime('%d.%m.%Y')
        break
    except ValueError:
        print('Неверный формат даты')


def valid_date(date):
    valid_data_list = []
    todady = datetime.date.today()
    date = date.split('.')
    for i in date:
        valid_data_list.append(int(i))
    date_time = datetime.date(valid_data_list[2], valid_data_list[1], valid_data_list[0])
    age = str((todady - date_time) / 365)
    delta = age.split(',')
    return delta[0]


print(birthday)
print(type(birthday))
print('-' * 30)

print(datetime.date.today())
print(type(datetime.date.today()))
print('-' * 30)
print(valid_date(birthday))
print(type(valid_date(birthday)))