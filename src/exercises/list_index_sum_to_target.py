from typing import List, Tuple


def list_index_sum_to_target(nums: List[int], target: int) -> Tuple[int, int]:
    ...


def test_list_index_sum_to_target():
    # nums on aina järjestyksessä, ratkaisu on aina olemassa

    nums = [1, 2, 4, 8]
    assert list_index_sum_to_target(nums, 2) == (0, 0)      # 1+1=2
    assert list_index_sum_to_target(nums, 3) == (0, 1)      # 1+2=3
    assert list_index_sum_to_target(nums, 5) == (0, 2)      # 1+4=5
    assert list_index_sum_to_target(nums, 12) == (2, 3)     # 4+8=12
