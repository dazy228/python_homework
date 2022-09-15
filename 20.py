import time


class Auto(object):
    brand = 'not specified'
    age = 'not specified'
    color = 'not specified'
    mark = 'not specified'
    weight = 'not specified'

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


class Truck(Auto):
    max_load = 'not specified'

    def move(self):
        print('attention')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


truck = Truck('BMW', 12, 'BMW')
truck.move()
truck.load()


class Car(Auto):
    max_speed = 498

    def move(self, max_speed=498):
        super().move()
        print(f'max speed is {max_speed}')


car = Car('BMW', 12, 'BMW')
car.move()