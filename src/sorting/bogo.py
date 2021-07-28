from helpers import benchmark, generate_random_list, generic_test

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


NAME = 'Bogo sort'

test_bogo = partial(
    generic_test,
    NAME,
    bogo,
    length=5,
)

bogo_benchmark = partial(
    benchmark,
    'Bogo sort',
    bogo,
    10,
)
