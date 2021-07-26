from typing import Set
from math import sqrt


def brute_force(num: int) -> Set[int]:
    collector = set()
    for i in range(2, num + 1):
        # 1 ei ole alkuluku
        # range ei ota yläpäätä mukaan, jonka takia +1
        if num % i == 0:
            collector.add(i)

    return collector


def recursive_solution(num: int) -> Set[int]:
    factors = set()
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            for j in [i, num//i]:
                if sub_factors := recursive_solution(j):
                    factors |= sub_factors
                else:
                    factors.add(j)

    return factors


def stackoverflow_solution(num: int) -> Set[int]:
    # Kiitokset Dentolle tästä
    # https://stackoverflow.com/questions/11924249/finding-prime-factors/11924315#11924315

    collector = set()

    i = 2
    while i**2 <= num:
        if num % i == 0:
            collector.add(i)
            num /= i
        else:
            i += 1

    if num > 1:
        collector.add(num)

    return collector
