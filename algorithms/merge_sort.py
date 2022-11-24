def sort_subarray(numbers, start, stop):
    if start > stop:
        return None
    half =  (stop + start) // 2
    sorted_left = sort_subarray(numbers, start, half)
    sorted_right = sort_subarray(numbers, half, stop)
    return merge(sorted_left, sorted_right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i != len(left) - 1 and j != len(right) - 1:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result


def sort(numbers):
    sort_subarray(numbers, 0, len(numbers))


sort([6, 5, 12, 10, 9, 1])
