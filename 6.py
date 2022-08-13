import random


def welcome_to_my_game():
    print(f"Отлично, {name}, я загадал число между 1 и 30. Сможешь угадать?:)")
    print("У тебя есть 6 попыток, погнали!")


def condition_set():
    if number < random_num:
        print("Твоё число меньше того, что я загадал:)")
    if number > random_num:
        print("Твоё число больше загаданного!")


def you_win():
    if number == random_num:
        print("-" * 50)
        print(f"Ух ты, {name}! Ты угадал число использовав кол-во попыток: {number_of_attempts}!")
        print("-" * 50)


def you_lose():
    if number_of_attempts >= 6:
        print("-" * 50)
        print(f"А вот и не угадал:( Я загадал число: {random_num}(((")
        print("-" * 50)


name = input("Привет! Как тебя зовут? ").title()
number_of_attempts = 0
random_num = random.randint(1, 30)

welcome_to_my_game()

while number_of_attempts < 6:
    number = int(input("Введите число: "))
    number_of_attempts += 1
    condition_set()
    if number == random_num:
        break
you_win()
you_lose()