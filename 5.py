# su = sum([i*i*i for i in range(1, n+1)])
# print("Result: ", su)
# --------------------------------------
value = int(input("Введите целое число: "))
result = 0
i = 1
item = 1
print("-----method for-----")
for item in range(1, value+1):
    if item % 3 == 0:
        continue
    i = item ** 3
    result += i
print(f"Ответ: {result}")

print("----method while----")
while i <= value:
    if i % 3 == 0:
        continue
    item = i**3
    i += 1
print(f"Ответ: {result}")
"""Програма посчитает сумму кубов всех целых чисел от 1 до n(включая n). Исключения составляют все числа кратные цифре 3"""

