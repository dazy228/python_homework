def replace_number(number):
    number = number.replace(',', '')
    number = number.replace('.', '')
    number = number.replace('-', '')
    try:
        number = int(number)
        return number
    except:     # подскажите пожалуйста почему у меня подчёркивает эту строку жёлтым, хотя она работает замечательно!
        number = str(number)
        return number


def digit_check(number):
    if type(number_2) is int:
        if number.isdigit():
            return f'Вы ввели положительное число: {number}'
        elif number.find('-') >= 0:
            if number.find('.') < 0 and number.find(',') < 0:
                if number.index('-') == 0:
                    if type(number_2) is int:
                        return f'Вы ввели отрицательное число: {number}'
                    else:
                        return f'Вы ввели не корректное число число: {number}'
                else:
                    return f'Вы ввели не корректное число число: {number}'
            else:
                return f'Вы ввели отрицательное дробное число: {number}'
        elif number.find('.') >= 0 or number.find(',') >= 0:
            return f'Вы ввели дробное число число: {number}'
    elif type(number_2) is str:
        return f'Вы ввели не корректное число: {number}'


while True:
    input_str = input("Введите число или сделайте выход ('выход', 'exit', 'quit', 'e' или 'q'): ")
    if input_str.lower() in ['выход', 'exit', 'quit', 'e', 'q']:
        print(f'Вы вышли!(')
        break
    else:
        number_2 = replace_number(input_str)    # Делаю из строки число убирая ".", ",", "-". если это можно сделать
        # print(type(number_2))
        print(digit_check(input_str))   # печатаю функцию которая умеет распознавать введённые числа