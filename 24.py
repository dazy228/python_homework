
def geometric_progression():
    a = 1
    q = int(input("Введите знаменатель прогрессии: "))
    n = int(input("Введите количество членов прогрессии: "))
    if q >= 1 and n >= 1:
        for item in range(n):
            yield a * q ** item
    else:
        print("\n                  ---Неверные данные!---")
        print("Знаменатель и количество членов прогрессии должны быть больше 1")


for i in geometric_progression():
    print(i)
