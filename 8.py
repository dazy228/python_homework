number = int(input("Введите число: "))

even_odd = lambda n: print(f'Число "{number}" чётное') if n % 2 == 0 else print(f'Число "{number}" не чётное')
even_odd(number)
