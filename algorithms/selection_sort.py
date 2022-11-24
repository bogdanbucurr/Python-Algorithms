from curs1.bubble_sort import generator_randoms
from curs1.decorators import Duration


@Duration
def sort(numbers):
    result = []
    while len(numbers) > 0:
        minimum = min(numbers)
        result.append(minimum)
        numbers.remove(minimum)
    return result

def remove_duplicates(numbers):
    return list(set(numbers))


if __name__ == '__main__':
    elemente = list(generator_randoms(10000))
    sorted_ = sort(elemente)
    print(remove_duplicates(sorted_))