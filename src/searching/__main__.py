from random import choice
from linear import linear
from binary import binary
from helpers import benchmark, generate_random_list

from tabulate import tabulate

from typing import List


def main():
    # All sorts are done in an ascending order
    tests()
    benchmarks()


def benchmarks():
    def default_index(search_space: List[int], target: int) -> int:
        return search_space.index(target)

    print(tabulate([
        benchmark(
            'Unsorted linear search',
            linear,
            10000,
        ),
        benchmark(
            'Sorted linear search',
            linear,
            10000,
            sorted,
        ),
        benchmark(
            'Binary search',
            binary,
            10000,
            sorted,
        ),
        benchmark(
            'Python builtin "index" unsorted',
            default_index,
            10000,
            sorted,
        ),
        benchmark(
            'Python builtin "index" sorted',
            default_index,
            10000,
        ),
    ], headers=['Algoritmi', 'Kippauspiste', '+-'],
    ))


def tests():
    random_list = generate_random_list(10, upper_bound=100)
    random_item = choice(random_list)
    random_item_index = random_list.index(random_item)

    print('Testing unsorted linear search')
    assert random_item_index == linear(random_list, random_item)

    print('Testing sorted linear search')
    random_list.sort()
    random_item_index = random_list.index(random_item)
    assert random_item_index == linear(random_list, random_item)

    print('Testing binary search')
    assert random_item_index == binary(random_list, random_item)


if __name__ == '__main__':
    main()
