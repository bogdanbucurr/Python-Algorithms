from base_sort import BaseSort
from util import Duration, generator_randoms


@Duration
def sort(numbers):
    result = []
    while len(numbers) > 0:
        minimum = min(numbers)
        result.append(minimum)
        numbers.remove(minimum)
    return result

class SelectionSort(BaseSort):
    def __init__(self):
        super().__init__('Selection Sort', sort)

class SelectionSort(BaseSort):
    def __init__(self):
        super().__init__('Selection Sort', sort)


if __name__ == '__main__':
    elemente = list(generator_randoms(1000))
    sorted_ = sort(elemente)
