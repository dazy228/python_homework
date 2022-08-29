from datetime import datetime
import time


def my_decorator(func):
    def the_wrapper():
        print(f'-' * 50)
        after = datetime.now()
        time.sleep(1.5)
        func()
        before = datetime.now()
        print(f'-' * 50)
        print(f'function running time: {before - after}')

    return the_wrapper


@my_decorator
def hello_world():
    print('Whether he was joking or not... is unknown.')


print(hello_world())