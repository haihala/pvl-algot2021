from typing import List
from time import time


def linear(search_space: List[int], target: int) -> int:
    for index, value in enumerate(search_space):
        if value == target:
            return index
