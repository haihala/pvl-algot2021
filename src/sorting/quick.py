from helpers import benchmark, generate_random_list

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


def test_quick():
    items = generate_random_list(10)
    result = quick(items[:], True)
    assert result == sorted(items), result


quick_benchmark = partial(
    benchmark,
    'Quick sort',
    quick,
    10000,
)
