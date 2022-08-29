from datetime import datetime
import time


def my_decorator(func):
    def the_wrapper():
        print(f'-' * 50)
        after = datetime.now()
        func()
        before = datetime.now()
        print(f'-' * 50)
        print(f'Function running time: {before - after}')

    return the_wrapper


@my_decorator
def first_func():
    time.sleep(1.5)
    print('Whether he was joking or not... is unknown.')


@my_decorator
def second_func():
    time.sleep(1.5)
    print('Look here, if this is some kind of macabre joke...')


print(first_func())
print(second_func())