while True:
    name = input("Введите своё имя: ", ).title()
    if name.isalpha():
        break
    else:
        print("Имя не может состоять из цифр, попробуйте ещё раз!")

while True:
    age = input("Введите свой возраст: ", )
    if not age.isdigit() or int(age) <= 0:
        print("Ошибка, повторите ввод!")
    elif int(age) < 10:
        print(f"Привет, шкет {name}")
        print("-------------------------")

    elif int(age) <= 18:
        print(f"Как жизнь {name}?")
        print("-------------------------")
    elif int(age) < 100:
        print(f"Что желаете {name}?")
        print("-------------------------")
    else:
        print(f"{name}, вы лжете - в наше время столько не живут...")
        print("-------------------------")
    answer = input(f"{name}, желаете выйти? (Д/Y) - ").upper()
    if answer in ("Д", "Y"):
        break