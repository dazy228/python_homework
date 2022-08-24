from datetime import datetime
import time


def my_decorator(func):
    def the_wrapper():
        time.sleep(1.5)
        print(f'time before - {datetime.now()}')
        time.sleep(1.5)
        func()

    return the_wrapper


def my_decorator_2(func):
    def the_wrapper():
        func()
        time.sleep(1.5)
        print(f'time after - {datetime.now()}')

    return the_wrapper


@my_decorator
@my_decorator_2
def hello_world():
    print('DATETIME')


hello_world()