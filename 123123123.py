def recognize(word: str):
    word = word.replace(",", ".", 1)
    try:
        word.replace(",", ".", 1)
        if float(word) == 0:
            return f"Вы ввели число {int(float(word))}"
        elif "." in word:
            return "Вы ввели {} дробное число {}".format("положительное" if float(word) > 0 else "отрицательное", float(word))
        else:
            return "Вы ввели {} целое число {}".format("положительное" if int(word) > 0 else "отрицательное", int(word))

    except:
        return f"Вы ввели не корректное число: {word}"


def recognize_2(word: str):
    word = word.replace(",", ".", 1)
    if not word.replace(".", "", 1).replace("-", "", 1).isdigit():
        return f"Вы ввели не корректное число: {word}"
    elif float(word) == 0:
        return f"Вы ввели число {int(float(word))}"
    elif "." in word:
        return "Вы ввели {} дробное число {}".format("положительное" if float(word) > 0 else "отрицательное", float(word))
    else:
        return "Вы ввели {} целое число {}".format("положительное" if int(word) > 0 else "отрицательное", int(word))


while True:
    input_word = input("Введите число: ")
    if input_word.lower() in ("выход", "exit", "quit", "e", "q"):
        break

    print(recognize(input_word))
    print(recognize_2(input_word))