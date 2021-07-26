from typing import List


def sorting_solution(nums: List[int]) -> int:
    nums.sort()
    return nums[-1]


def manual_solution(nums: List[int]) -> int:
    max_so_far = nums[0]
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far


def the_right_solution(nums: List[int]) -> int:
    return max(nums)
