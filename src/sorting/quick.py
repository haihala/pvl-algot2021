from helpers import benchmark, generate_random_list, generic_test

from typing import List, Optional
from functools import partial


def quick(nums: List[int], debug: Optional[bool] = False) -> List[int]:
    if len(nums) <= 1:
        return nums
    elif len(nums) == 2:
        return [min(nums), max(nums)]

    pivot = nums[-1]
    low = 0
    high = 2

    while low <= len(nums)-high:
        if nums[-high] > pivot:
            high += 1
        elif nums[low] < pivot:
            low += 1
        else:
            # nums[low] is more than pivot
            # nums[high] is less than pivot
            # Swap them so they are on the correct sides
            nums[low], nums[-high] = nums[-high], nums[low]

            # After the swap, both of them are on the correct side
            low += 1
            high += 1

    nums.insert(low, nums.pop())

    return quick(nums[:low], debug) + [pivot] + quick(nums[low+1:], debug)


NAME = 'Quick sort'

test_quick = partial(
    generic_test,
    NAME,
    quick,
)

quick_benchmark = partial(
    benchmark,
    NAME,
    quick,
    10000,
)
