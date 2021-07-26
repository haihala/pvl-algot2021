from multiprocessing import Process
import multiprocessing
from numpy.random import randint as random_numpy_array
from time import time
from dataclasses import dataclass
from typing import List, Optional, Callable


def generate_random_list(
    length: int,
    lower_bound: Optional[int] = 0,
    upper_bound: Optional[int] = 1_000_000_000,
) -> List[int]:
    return random_numpy_array(lower_bound, upper_bound, length).tolist()


def benchmark(
    name: str,
    sort_func: Callable[
        [List[int]],
        List[int]
    ],
    initial_length,
    timeout: Optional[float] = 1.0,
    strikes_before_out: Optional[int] = 3,
):
    print(f'Benchmarking {name}')
    length = initial_length
    strikes = []
    while len(strikes) < strikes_before_out:
        result = run_sort(sort_func, name, length, timeout)
        if result.timeout:
            strikes.append(length)
            length = int(length/1.1)
        else:
            length = int(max(
                length * 1.1,
                length / result.time_share_used,
            ))

    return (name, int(sum(strikes)/strikes_before_out))


def run_sort(
    sort_func: Callable[
        [List[int]],
        List[int]
    ],
    name: str,
    length: int,
    timeout: float,
):
    process = Process(
        target=sort_func,
        name=name,
        args=[
            generate_random_list(length)
        ]
    )
    start_time = time()
    process.start()
    process.join(timeout)
    process.terminate()

    return RunResult((time()-start_time)/timeout, process.exitcode is None)


@dataclass
class RunResult:
    time_share_used: float
    timeout: bool
