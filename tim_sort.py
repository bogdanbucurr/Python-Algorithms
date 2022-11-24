from algorithms.bubble_sort import generator_randoms
from algorithms.decorators import Duration


@Duration
def sort(number):
    number.sort()
    return number

if __name__ == '__main__':
    elemente = list(generator_randoms(10000))
    sorted_ = sort(elemente)
    print(sorted_)