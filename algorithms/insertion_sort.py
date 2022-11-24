from algorithms.bubble_sort import generator_randoms
from algorithms.decorators import Duration


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


if __name__ == '__main__':
    elemente = list(generator_randoms(10000))
    sorted_ = sort(elemente)
    print((sorted_))
