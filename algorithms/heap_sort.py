from heapq import heappush, heappop

from curs1.bubble_sort import generator_randoms
from curs1.decorators import Duration


def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


@Duration
def sort(numbers):
    return heapsort(numbers)


if __name__ == '__main__':
    elemente = list(generator_randoms(10000))
    sorted_ = sort(elemente)
    print(sorted_)
