from sys import argv as command_line_args

from tabulate import tabulate

from bogo import bogo_benchmark, test_bogo
from stalin import stalin_benchmark, test_stalin
from bubble import bubble_benchmark, test_bubble
from insertion import insertion_benchmark, test_insertion
from quick import quick_benchmark, test_quick
from default import sorted_benchmark


def main():
    if 'test' in command_line_args[1:]:
        tests()
    if 'bench' in command_line_args[1:]:
        benchmarks()


def benchmarks():
    print(tabulate([
        bogo_benchmark(),
        stalin_benchmark(),
        bubble_benchmark(),
        insertion_benchmark(),
        quick_benchmark(),
        sorted_benchmark(),
    ], headers=['Algoritmi', 'Kippauspiste', '+-'],
    ))


def tests():
    test_bogo()
    test_stalin()
    test_bubble()
    test_insertion()
    test_quick()


if __name__ == '__main__':
    main()
