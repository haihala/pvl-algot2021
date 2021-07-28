from threading import Thread
from math import inf
from numpy.random import randint as random_numpy_array
from time import time
from random import choice
from typing import List, Optional, Callable


def generic_test(
    name: str,
    func: Callable[
        [List[int]],
        List[int]
    ],
    preprocessor: Optional[
        Callable[
            [List[int]],
            List[int],
        ]
    ] = None,
):
    print(f'Testing {name}', end='')
    items = generate_random_list(10)

    if preprocessor:
        items = preprocessor(items)

    target = choice(items)

    expected = items.index(target)
    actual = func(items, target)

    assert expected == actual, (expected, actual)
    print(' - Passed')


def generate_random_list(
    length: int,
    lower_bound: Optional[int] = 0,
    upper_bound: Optional[int] = 1_000_000_000,
) -> List[int]:
    if length > 100_000_000:
        # Oppimiskokemus.
        # Lisätty sen jälkeen kun puolitushaku havaittiin niin nopeaksi että
        # koneessa ei ollut tarpeeksi muistia niin pitkälle listalle että se timeouttaisi.
        # Listan sorttaaminen etukäteen oli myös aika iso ongelma.
        raise MemoryError
    return random_numpy_array(lower_bound, upper_bound, length).tolist()


def adjust_magnitude(old: int, increase: bool) -> int:
    if increase:
        return 10*old
    else:
        return int(old/10)


def weighted_average(upper: int, lower: int) -> int:
    return int((upper+lower*2)/3)


def output(upper: int, lower: int) -> str:
    average = int((upper+lower)/2)
    deviation = int((upper-lower)/2)
    return average, f'+/- {deviation}'


def benchmark(
    name: str,
    search_func: Callable[
        [List[int]],
        List[int]
    ],
    initial_length: int,
    preprocessor: Optional[
        Callable[
            [List[int]],
            List[int],
        ]
    ] = None,
    repeated_searches: Optional[int] = 1000,
    timeout: Optional[float] = 1,
    bisections: Optional[int] = 10,
):
    print(f'Benchmarking {name}')
    bisections_completed = 0
    length = initial_length
    highest_success = 0
    lowest_failure = inf

    while bisections_completed < bisections:
        try:
            ran_without_timeout = run_search(
                search_func,
                name,
                length,
                repeated_searches,
                timeout,
                preprocessor,
            )
        except MemoryError:
            return (name, 'Muisti safeguard kicks in')

        if ran_without_timeout:
            highest_success = length
        else:
            lowest_failure = length

        next_length = adjust_magnitude(length, ran_without_timeout)
        if lowest_failure > next_length > highest_success:
            length = next_length
        else:
            length = weighted_average(lowest_failure, highest_success)
            bisections_completed += 1
    return (name, *output(lowest_failure, highest_success))


def run_search(
    search_func: Callable[
        [List[int]],
        List[int]
    ],
    name: str,
    length: int,
    repeated_searches: int,
    timeout: float,
    preprocessor: Optional[Callable[[List[int]], List[int]]] = None,
):
    random_list = generate_random_list(length)

    start_time = time()
    if preprocessor:
        random_list = preprocessor(random_list)

    targets = [choice(random_list) for _ in range(repeated_searches)]

    for repetition in range(repeated_searches):
        process = Thread(
            target=search_func,
            name=name,
            args=(
                random_list,
                targets[repetition],
            ),
            daemon=True,
        )
        process.start()
        process.join(timeout/repeated_searches)

        if process.is_alive():
            return False
    time_spent = (time()-start_time)
    return time_spent < timeout
