from helpers import benchmark, generic_test

from typing import List
from functools import partial


def insertion(nums: List[int]) -> List[int]:
    output = [nums[0]]

    for i in nums[1:]:
        for output_index, value in enumerate(output):
            if value > i:
                output.insert(output_index, i)
                break
        else:
            output.append(i)

    return output


NAME = 'Insertion sort'

test_insertion = partial(
    generic_test,
    NAME,
    insertion,
)

insertion_benchmark = partial(
    benchmark,
    NAME,
    insertion,
    10000,
)
