from heapq import heappush, heappop
from base_sort import BaseSort
from util import generator_randoms
from util import Duration


def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


@Duration
def sort(numbers):
    return heapsort(numbers)


class HeapSort(BaseSort):
    def __init__(self):
        super().__init__('Heap Sort', sort)


if __name__ == '__main__':
    elemente = list(generator_randoms(1000))
    sorted_ = sort(elemente)
