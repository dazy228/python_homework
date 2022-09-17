class Tusk(object):
    name = 'Tusk'
    numbers = 0

    def __init__(self, color='black', weight=1.73):
        self.color = color
        self.weight = weight

    @staticmethod
    def move():
        print('move')

    @staticmethod
    def hours():
        print(12+7)

    @classmethod
    def rename(cls):
        cls.name = 'Tusk_2'
        print(cls.name)

    @classmethod
    def number(cls):
        cls.numbers += 1
        print(cls.numbers)


tusk_1 = Tusk()
tusk_2 = Tusk()
print(tusk_1.name, tusk_2.name)
tusk_1.move()
tusk_1.hours()
tusk_2.rename()
print(tusk_1.numbers)
tusk_2.number()
tusk_1.number()

print('-' * 10)
print(tusk_1.name, tusk_2.name)
tusk_2.move()
tusk_2.hours()
