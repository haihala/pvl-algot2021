from helpers import benchmark, generate_random_list

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


NAME = 'Stalin sort'


def _test_stalin():
    print(f'Testing {NAME}', end='')

    # Stalin tuhoaa alkioita niin ei voi käyttää generic
    items = generate_random_list(10)
    result = stalin(items[:])

    assert all(result[i] < result[i+1] for i in range(len(result)-1))
    assert len(result) <= len(items)
    print(' - Passed')


# This is done so that vscode uses consistent coloring
# It isn't what you'd call good code, but it saves 20 seconds from the lecture
# Don't actually ever do this
test_stalin = _test_stalin


stalin_benchmark = partial(
    benchmark,
    NAME,
    stalin,
    100000,
)
