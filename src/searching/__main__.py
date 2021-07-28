from sys import argv as command_line_args

from tabulate import tabulate

from linear import benchmark_sorted_linear, benchmark_unsorted_linear, test_sorted_linear, test_unsorted_linear
from binary import benchmark_binary, test_binary
from default import benchmark_sorted_default, benchmark_unsorted_default


def main():
    if 'test' in command_line_args[1:]:
        tests()
    if 'bench' in command_line_args[1:]:
        benchmarks()


def benchmarks():
    print(tabulate([
        benchmark_sorted_linear(),
        benchmark_unsorted_linear(),
        benchmark_binary(),
        benchmark_sorted_default(),
        benchmark_unsorted_default(),
    ], headers=['Algoritmi', 'Kippauspiste', '+-'],
    ))


def tests():
    test_sorted_linear()
    test_unsorted_linear()
    test_binary()


if __name__ == '__main__':
    main()
