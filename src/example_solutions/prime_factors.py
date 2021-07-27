from typing import Set
from math import sqrt


def brute_force(num: int) -> Set[int]:
    collector = set()
    for i in range(2, num+1):
        # 1 ei ole alkuluku, jonka tähden aloitetaan range 2:sta
        if num % i == 0:
            # Tässä kohtaa lisätään kaikki tekijät
            collector.add(i)

    # Tässä kohtaa suodatetaan ne pois jotka eivät ole alkulukuja
    return set(
        filter(
            lambda x: not any(
                x % i == 0 and x is not i
                for i in collector
            ),
            collector,
        )
    )


def recursive_solution(num: int) -> Set[int]:
    collector = {
        j
        for i in filter(lambda x: num % x == 0, range(2, int(sqrt(num))+1))
        for j in {i, num//i}
        if recursive_solution(j) == {j}
    }
    if len(collector) == 0:
        collector.add(num)
    collector.discard(1)
    return collector


def stackoverflow_solution(num: int) -> Set[int]:
    # Kiitokset Dentolle tästä
    # https://stackoverflow.com/questions/11924249/finding-prime-factors/11924315#11924315

    collector = set()

    i = 2
    # i**2 == i*i == i^2(python ei tue tätä)
    while i**2 <= num:
        if num % i == 0:
            collector.add(i)
            num /= i
        else:
            i += 1

    if num > 1:
        collector.add(num)

    return collector
