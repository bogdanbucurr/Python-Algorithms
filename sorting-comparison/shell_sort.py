from base_sort import BaseSort
from util import Duration, generator_randoms


@Duration
def shell_sort(numbers):
    interval = len(numbers) // 2

    while interval > 0:
        for value in range(interval, len(numbers)):
            temp = numbers[value]
            j = value
            while j >= interval and numbers[j - interval] > temp:
                numbers[j] = numbers[j - interval]
                j -= interval
            numbers[j] = temp
        interval = interval // 2
    return numbers


class ShellSort(BaseSort):
    def __init__(self):
        super().__init__('Shell Sort', shell_sort)

if __name__ == '__main__':
    elemente = list(generator_randoms(1000))
    sorted_ = shell_sort(elemente)