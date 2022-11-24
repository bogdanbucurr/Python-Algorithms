from curs1.bubble_sort import generator_randoms
from curs1.decorators import Duration


def top_down_merge(a, i_begin, i_middle, i_end, b):
    i = i_begin
    j = i_middle
    for k in range(i_begin, i_end):
        if i < i_middle and (j >= i_end or a[i] <= a[j]):
            b[k] = a[i]
            i = i + 1
        else:
            b[k] = a[j]
            j = j + 1
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




if __name__ == '__main__':
    #print(top_down_merge_sort([9, 1, 28, 55], [], 4))
    elemente = list(generator_randoms(10000))
    sorted_ = sort(elemente)
    print((sorted_))