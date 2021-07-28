from functools import partial
from typing import List

from helpers import benchmark


def default_index(search_space: List[int], target: int) -> int:
    return search_space.index(target)


benchmark_sorted_default = partial(
    benchmark,
    'Python builtin "index" unsorted',
    default_index,
    10000,
    sorted,
)

benchmark_unsorted_default = partial(
    benchmark,
    'Python builtin "index" sorted',
    default_index,
    10000,
)
