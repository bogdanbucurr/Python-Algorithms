from base_sort import BaseSort
from util import Duration


@Duration
def sort(numbers):
    pos = 0
    while pos < len(numbers):
        if pos == 0 or numbers[pos] >= numbers[pos - 1]:
            pos = pos + 1
        else:
            temp = numbers[pos]
            numbers[pos] = numbers[pos - 1]
            numbers[pos - 1] = temp
            pos = pos - 1
    return numbers


class GnomeSort(BaseSort):
    def __init__(self):
        super().__init__('Gnome Sort', sort)
