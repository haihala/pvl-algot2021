from functools import partial
from typing import List

from helpers import generic_test, benchmark


def linear(search_space: List[int], target: int) -> int:
    for index, value in enumerate(search_space):
        if value == target:
            return index


SORTED_NAME = 'Sorted linear search'
UNSORTED_NAME = 'Unsorted linear search'

test_sorted_linear = partial(
    generic_test,
    SORTED_NAME,
    linear,
    sorted
)

test_unsorted_linear = partial(
    generic_test,
    UNSORTED_NAME,
    linear,
)

benchmark_sorted_linear = partial(
    benchmark,
    SORTED_NAME,
    linear,
    10000,
    sorted,
)

benchmark_unsorted_linear = partial(
    benchmark,
    UNSORTED_NAME,
    linear,
    10000,
)
