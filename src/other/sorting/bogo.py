from helpers import benchmark, doubler, generate_random_list

from typing import List
from random import shuffle
from functools import partial


def bogo(nums: List[int]) -> List[int]:
    while True:
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                break
        else:
            # Goes in here if the for loop isn't broken
            return nums
        shuffle(nums)


def test_bogo():
    items = generate_random_list(5)
    assert bogo(items[:]) == sorted(items)


bogo_benchmark = partial(benchmark, 'Bogo sort', bogo, doubler(4))
