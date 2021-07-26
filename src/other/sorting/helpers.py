from multiprocessing import Process
from numpy.random import randint as random_numpy_array
from time import time, sleep
from typing import Iterable, List, Optional, Callable


def generate_random_list(
    length: int,
    lower_bound: Optional[int] = 0,
    upper_bound: Optional[int] = 1_000_000_000,
) -> List[int]:
    return random_numpy_array(lower_bound, upper_bound, length).tolist()


def doubler(initial: int) -> int:
    current = initial
    while True:
        yield current
        current *= 2


def benchmark(
    name: str,
    sort_func: Callable[
        [List[int]],
        List[int]
    ],
    list_lengths: Iterable[int] = doubler(1000),
    timeout: Optional[float] = 1.0,
):
    for target in list_lengths:
        job = Process(
            target=sort_func,
            name=name,
            args=[
                generate_random_list(target)
            ]
        )
        start_time = time()
        job.start()

        while job.is_alive():
            if time()-start_time > timeout:
                job.kill()
                job.join()
                print(f'{name} timed out with {target} items')
                return
            sleep(0.1)
        job.join()
        print(f'{name} took {time()-start_time:.2f}s with {target} items')
