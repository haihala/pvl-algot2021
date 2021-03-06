from helpers import benchmark, generic_test

from typing import List
from functools import partial


def bubble(nums: List[int]) -> List[int]:
    for done_index in range(len(nums), 0, -1):
        for i in range(1, done_index):
            left = nums[i-1]
            right = nums[i]

            nums[i-1] = min(left, right)
            nums[i] = max(left, right)

    return nums


NAME = 'Bubble sort'

test_bubble = partial(generic_test, NAME, bubble)

bubble_benchmark = partial(
    benchmark,
    NAME,
    bubble,
    1000,
)
