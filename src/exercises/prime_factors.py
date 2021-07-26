from typing import Set
from math import sqrt


def prime_factors(num: int) -> Set[int]:
    ...


def test_prime_factors():
    assert prime_factors(4) == {2}
    assert prime_factors(6) == {2, 3}
    assert prime_factors(30) == {2, 3, 5}
    assert prime_factors(100) == {2, 5}

    # {} on pythonissa tyhjä dict, joka ei ole yhtä suuri kuin tyhjä setti, niin pitää käyttää set()
    assert prime_factors(1) == set()
    assert prime_factors(3) == {3}
