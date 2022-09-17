# Создать программу-калькулятор в виде класса и несколько методов, как минимум сложение, вычитание, деление, умножение, возведение в степень и извлечение квадратного корня

class ZeroException(Exception):
    def __init__(self):
        super().__init__('Zero division. My custom exception')


class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        try:
            return int(self.a) + int(self.b)
        except ValueError:
            return str(self.a) + str(self.b)

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return 'Division by zero is not allowed'

    def pow(self):
        try:
            if self.b < 0:
                raise ZeroException
            return self.a ** self.b
        except ZeroException as err:
            return err

    def sqrt(self):
        return self.a ** (1 / 2)


calc = Calculator(25, -5)
print(f'sum - {calc.sum()}')
print(f'sub - {calc.sub()}')
print(f'mul - {calc.mul()}')
print(f'div - {calc.div()}')
print(f'pow - {calc.pow()}')
print(f'sqrt - {calc.sqrt()}')



