from helpers import benchmark, doubler, generate_random_list

from typing import List
from functools import partial


def stalin(nums: List[int]) -> List[int]:
    highest_value = nums[0]
    output = [highest_value]

    for i in nums:
        if i > highest_value:
            output.append(i)
            highest_value = i
    return output


def test_stalin():
    items = generate_random_list(10)
    # Stalin tuhoaa alkioita niin ei voi testata 'helposti' onko ne järjestyksessä
    result = stalin(items[:])

    assert all(result[i] < result[i+1] for i in range(len(result)-1))
    assert len(result) <= len(items)


stalin_benchmark = partial(benchmark, 'Stalin sort', stalin, doubler(1000))
