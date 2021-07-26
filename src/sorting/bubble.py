from helpers import benchmark, generate_random_list

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


def test_bubble():
    items = generate_random_list(10)
    result = bubble(items[:])
    assert result == sorted(items), result


bubble_benchmark = partial(benchmark, 'Bubble sort', bubble, 1000)
