from base_sort import BaseSort
from util import Duration, generator_randoms


@Duration
def sort(numbers):
    numbers.sort()
    return numbers


class TimSort(BaseSort):
    def __init__(self):
        super().__init__('Tim Sort', sort)

class TimSort(BaseSort):
    def __init__(self):
        super().__init__('Tim Sort', sort)

if __name__ == '__main__':
    elemente = list(generator_randoms(10000))
    sorted_ = sort(elemente)
