import time
from abc import ABC


class BaseSort(ABC):
    def __init__(self, name, sorting_method):
        self.name = name
        self.sorting_method = sorting_method

    def run(self, numbers):
        length = len(numbers)
        t1 = time.time()
        self.sorting_method(numbers)
        t2 = time.time()
        delta_t = t2 - t1
        return self.name, length, delta_t

