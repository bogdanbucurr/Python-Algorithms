from base_sort import BaseSort
from util import Duration, generator_randoms


def top_down_merge(a, i_begin, i_middle, i_end, b):
    i = i_begin
    j = i_middle
    for k in range(i_begin, i_end):
        if i < i_middle and (j >= i_end or a[i] <= a[j]):
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
    return b


def top_down_split_merge(b, i_begin, i_end, a):
    if i_end - i_begin <= 1:
        return a
    i_middle = (i_end + i_begin) // 2
    top_down_split_merge(a, i_begin, i_middle, b)
    top_down_split_merge(a, i_middle, i_end, b)
    return top_down_merge(b, i_begin, i_middle, i_end, a)


def top_down_merge_sort(a, b, n):
    b.extend(a)

    return top_down_split_merge(b, 0, n, a)


@Duration
def sort(numbers):
    return top_down_merge_sort(numbers, [], len(numbers))

class MergeSort(BaseSort):
    def __init__(self):
        super().__init__('Merge Sort', sort)


class MergeSort(BaseSort):
    def __init__(self):
        super().__init__('Merge Sort', sort)


if __name__ == '__main__':
    elemente = list(generator_randoms(1000))
    sorted_ = sort(elemente)
