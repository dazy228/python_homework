import time
from home_work19 import Auto


class Truck(Auto):
    max_load = 'not specified'

    def __init__(self, brand, age, mark, max_load,):
        super().__init__(self, brand, age, mark)
        self.max_load = max_load

    def move(self):
        print('attention')
        super().move()

    @staticmethod
    def load():
        time.sleep(1)
        print('load')
        time.sleep(1)


truck = Truck('BMW', 12, 'BMW', 1000)
truck.move()
truck.load()


class Car(Auto):
    max_speed = 498

    def move(self, max_speed=498):
        super().move()
        print(f'max speed is {max_speed}')


car = Car('BMW', 12, 'BMW')
car.move()