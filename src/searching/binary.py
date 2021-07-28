from functools import partial
from typing import List

from helpers import benchmark, generic_test


def binary(search_space: List[int], target: int) -> int:
    low_bound = 0
    high_bound = len(search_space)

    while True:
        test_index = (low_bound+high_bound)//2
        value = search_space[test_index]
        if value == target:
            return test_index
        elif value > target:
            high_bound = test_index
        else:
            low_bound = test_index


NAME = 'Binary search'

test_binary = partial(
    generic_test,
    NAME,
    binary,
    sorted
)

benchmark_binary = partial(
    benchmark,
    NAME,
    binary,
    10000,
    sorted,
)
