from base_sort import BaseSort
from util import Duration, generator_randoms

@Duration
def merge_sort_v2(numbers):
    if len(numbers) > 1:
        left = numbers[:len(numbers) // 2]
        right = numbers[len(numbers) // 2:]

        merge_sort_v2(left)
        merge_sort_v2(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
                k += 1
            else:
                numbers[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1

    return numbers


class MergeSort2(BaseSort):
    def __init__(self):
        super().__init__('Heap Sort', merge_sort_v2)


if __name__ == '__main__':
    elemente = list(generator_randoms(10000))
    sorted_ = merge_sort_v2(elemente)
