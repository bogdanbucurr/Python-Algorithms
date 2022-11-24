from base_sort import BaseSort
from util import Duration, generator_randoms



@Duration
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]
    less_than_pivot = []
    greater_than_pivot = []

    for i in numbers[1:]:
        if i <= pivot:
            less_than_pivot.append(i)
        else:
            greater_than_pivot.append(i)

    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

class QuickSort(BaseSort):
    def __init__(self):
        super().__init__('Quick Sort', quick_sort)


if __name__ == '__main__':
    elemente = list(generator_randoms(1000))
    sorted_ = quick_sort(elemente)
