import csv
import sys

from bubble_sort import BubbleSort
from gnome_sort import GnomeSort
from heap_sort import HeapSort
from insertion_sort import InsertionSort
from merge_sort import MergeSort
from merge_sort_v2 import MergeSort2
from quick_sort import QuickSort
from selection_sort import SelectionSort
from shell_sort import ShellSort
from tim_sort import TimSort
from util import generator_randoms

sys.setrecursionlimit(1000000000)
counts = [
    10, 100, 1000, 10000, 100000, 1000000
]
lists = [generator_randoms(count) for count in counts]

sorters_dic = {
    BubbleSort(): lists[:-2],
    HeapSort(): lists,
    InsertionSort(): lists[:-2],
    MergeSort2(): lists,
    SelectionSort(): lists[:-2],
    TimSort(): lists,
    QuickSort(): lists[:-2],
    ShellSort(): lists,
    GnomeSort(): lists,

}

# sorters = [
#     BubbleSort(), HeapSort(), InsertionSort(), MergeSort(), SelectionSort(),
#     TimSort(),
#     MergeSort2(),
#     QuickSort(),
#     ShellSort()
# ]

result = []

for sorter in sorters_dic:
    row_result = [sorter.name]
    for numbers in sorters_dic[sorter]:
        name, length, time_ = sorter.run(numbers)
        row_result.append(time_)
        print(name, length, time_)
    result.append(row_result)

with open('sortari.csv', 'w', newline='') as csvfile:
    spanwriter = csv.writer(csvfile)
    # header row
    header = [' ']
    header.extend(counts)
    spanwriter.writerow(header)
    # each sort
    for row in result:
        spanwriter.writerow(row)
