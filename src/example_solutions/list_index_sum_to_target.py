from typing import List, Tuple


def brute_force_solution(nums: List[int], target: int) -> Tuple[int, int]:
    for index1, value1 in enumerate(nums):
        for index2, value2 in enumerate(nums):
            if value1+value2 == target:
                return (index1, index2)


def bounds_solution(nums: List[int], target: int) -> Tuple[int, int]:
    low = 0
    high = len(nums) - 1
    while low != high:
        current = nums[low] + nums[high]
        if current == target:
            return (low, high)

        if current > target:
            high -= 1
        else:
            low += 1

    # You never should've come here, jossain on bugi


def dict_solution(nums: List[int], target: int) -> Tuple[int, int]:
    collector = {}
    for index, value in enumerate(nums):
        if value in collector:
            return (collector[value], index)

        if value == target/2:
            return (index, index)

        collector[target-value] = index
