
while True:
    name = input("Введите своё имя: ", ).title()
    if not name.isdigit():
        break
    else:
        print("Имя не может состоять из цифр, попробуйте ещё раз!")

while True:
    age = input("Введите свой возраст: ", )
    if not age.isdigit() or int(age) <= 0:
        print("Ошибка, повторите ввод!")
    elif int(age) < 10:
        print(f"Привет, шкет {name}")
        print("---------------------")
        answer = input("Хотите выйти? (y/д): ")
        if answer in ("y", "д", "Y", "Д"):
            break
        else:
            continue
    elif int(age) <= 18:
        print(f"Как жизнь {name}?")
        print("---------------------")
        answer = input("Хотите выйти? (y/д): ")
        if answer in ("y", "д", "Y", "Д"):
            break
        else:
            continue
    else:
        print(f"{name}, вы лжете - в наше время столько не живут...")

