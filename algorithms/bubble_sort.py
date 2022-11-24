import random

#from decorators import Duration
from algorithms.decorators import Duration


@Duration
def sort(numbers):
    sorted_ = False
    while not sorted_:
        sorted_ = True
        for i in range(len(numbers) - 1):
            elem1 = numbers[i]
            elem2 = numbers[i + 1]
            if elem2 < elem1:
                numbers[i] = elem2
                numbers[i + 1] = elem1
                sorted_ = False
    return numbers

def generator_randoms(count):
    for i in range(count):
        yield random.randrange(1, 1000)


if __name__ == '__main__':
    elemente =list(generator_randoms(10000))
    sorted_ = sort(elemente)

