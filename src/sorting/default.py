from functools import partial

from helpers import benchmark

sorted_benchmark = partial(
    benchmark,
    'Python builtin "sorted"',
    sorted,
    100000,
)
