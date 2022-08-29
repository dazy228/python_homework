first_line = input('Введите любую строку: ')
second_line = input('Введите любую строку: ')
third_line = input('Введите любую строку: ')
fourth_line = input('Введите любую строку: ')

file = open('homework_15.txt', 'w')
try:
    file.write(f'{first_line}\n')
    file.write(f'{second_line}\n')
finally:
    file.close()

file = open('homework_15.txt', 'a')
try:
    file.write(f'{third_line}\n')
    file.write(f'{fourth_line}\n')
finally:
    file.close()
    # поясните на след. уроке как записывать в файл русские символы и тому подорбныее, я пробывал писать русский текст
    # и у меня были знаки вопроса и писало что не соответствует кодировке UTF-8!