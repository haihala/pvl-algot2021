from helpers import benchmark, generate_random_list

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


def test_insertion():
    items = generate_random_list(10)
    result = insertion(items[:])
    assert result == sorted(items), result


insertion_benchmark = partial(
    benchmark,
    'Insertion sort',
    insertion,
    10000,
)
