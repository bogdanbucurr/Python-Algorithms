from base_sort import BaseSort
from util import generator_randoms, Duration


@Duration
def sort(numbers):
    result = []
    for number in numbers:
        if len(result) == 0:
            result.append(number)
            continue
        for i in range(len(result)):
            elem = result[i]
            if number < elem:
                result.insert(i, number)
                break
            if i == len(result) - 1:
                result.append(number)
                break
    return result

class InsertionSort(BaseSort):
    def __init__(self):
        super().__init__('Insertion Sort', sort)


class InsertionSort(BaseSort):
    def __init__(self):
        super().__init__('Insertion Sort', sort)


if __name__ == '__main__':
    elemente = list(generator_randoms(1000))
    sorted_ = sort(elemente)
