# decorators sort
import random
import time


def generator_randoms(count):
    return [random.randrange(1, 1000) for i in range(count)]


def remove_duplicates(numbers):
    return list(set(numbers))


class Duration:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        t1 = time.time()
        result = self.func(*args, **kwargs)
        t2 = time.time()
        return result
