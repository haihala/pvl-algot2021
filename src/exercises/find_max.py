from typing import List


def find_max(nums: List[int]) -> int:
    ...


def test_find_max():
    assert find_max([1, 2, 3]) == 3
    assert find_max([1, 2, -3]) == 2
    assert find_max([-1, -2, -3]) == -1
