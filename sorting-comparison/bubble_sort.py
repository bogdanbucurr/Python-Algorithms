from base_sort import BaseSort
from util import Duration, generator_randoms


@Duration
def sort(numbers):
    sorted_ = False
    while not sorted_:
        sorted_ = True
        for i in range(len(numbers) - 1):
            elem1 = numbers[i]
            elem2 = numbers[i + 1]
            if elem2 < elem1:
                numbers[i] = elem2
                numbers[i + 1] = elem1
                sorted_ = False
    return numbers


class BubbleSort(BaseSort):
    def __init__(self):
        super().__init__('Bubble Sort', sort)





if __name__ == '__main__':
    elemente = list(generator_randoms(1000))
    # sorted_ = sort(elemente)
    name, length, time_ = BubbleSort().run(elemente)
    print(name, length, time_)


