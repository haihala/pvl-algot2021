from helpers import benchmark, doubler

from bogo import bogo_benchmark, test_bogo
from stalin import stalin_benchmark, test_stalin
from bubble import bubble_benchmark, test_bubble
from insertion import insertion_benchmark, test_insertion
from quick import quick_benchmark, test_quick


def main():
    # All sorts are done in an ascending order
    tests()
    benchmarks()


def benchmarks():
    bogo_benchmark()
    stalin_benchmark()
    bubble_benchmark()
    insertion_benchmark()
    quick_benchmark()
    benchmark(
        'Sorted',
        sorted,
        doubler(1000),
    )


def tests():
    print('Testing Bogo sort')
    test_bogo()

    print('Testing Stalin sort')
    test_stalin()

    print('Testing Bubble sort')
    test_bubble()

    print('Testing Insertion sort')
    test_insertion()

    print('Testing Quick sort')
    test_quick()


if __name__ == '__main__':
    main()
