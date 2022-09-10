class Auto(object):
    brand = str
    age = 0
    color = str
    mark = str
    weight = float

    def __init__(self, brand, age, mark, color='black', weight=1.73):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print('move')

    def birthday(self, age):
        self.age = age
        age += 1
        print(f'{age}')

    def stop(self):
        print('stop')


auto = Auto('BMW', 12, 'BMW')
auto.stop()
auto.move()
auto.birthday(0)
