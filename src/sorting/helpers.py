from threading import Thread
from math import inf
from numpy.random import randint as random_numpy_array
from typing import List, Optional, Callable


def generic_test(
    name: str,
    func: Callable[
        [List[int]],
        List[int]
    ],
    length: Optional[int] = 10,
):
    print(f'Testing {name}', end='')
    items = generate_random_list(
        length,

        # Small enough for collisions to occasionally happen and to be human readable
        upper_bound=100,
    )
    expected = sorted(items[:])
    actual = func(items[:])

    assert expected == actual, (expected, actual)
    print(' - Passed')


def generate_random_list(
    length: int,
    lower_bound: Optional[int] = 0,
    upper_bound: Optional[int] = 1_000_000_000,
) -> List[int]:
    if length > 10_000_000:
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
            ran_without_timeout = run_sort(
                search_func,
                name,
                length,
                timeout,
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


def run_sort(
    sort_func: Callable[
        [List[int]],
        List[int]
    ],
    name: str,
    length: int,
    timeout: float,
):
    random_list = generate_random_list(length)
    thread = Thread(
        target=sort_func,
        name=name,
        args=(
            random_list,
        ),
        daemon=True,
    )
    thread.start()
    thread.join(timeout)
    return not thread.is_alive()
