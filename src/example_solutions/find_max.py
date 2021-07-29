from typing import List


def brute_forces_solution(nums: List[int]) -> int:
    max_so_far = nums[0]
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far


def sorting_solution(nums: List[int]) -> int:
    return sorted(nums)[-1]


def builtin_solution(nums: List[int]) -> int:
    return max(nums)
