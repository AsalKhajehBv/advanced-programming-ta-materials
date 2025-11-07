"""
math_tools.operations
A collection of small math utilities.
"""

import math
import statistics
from typing import Iterable


def gcd(a: int, b: int) -> int:
    """Return greatest common divisor of a and b."""
    return math.gcd(a, b)

def lcm(a: int, b: int) -> int:
    """Return least common multiple of a and b."""
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)

def is_prime(n: int) -> bool:
    """Return True if n is prime (simple deterministic check for n >= 2)."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

def mean(data: Iterable[float]) -> float:
    """Return arithmetic mean of data."""
    seq = list(data)
    if len(seq) == 0:
        raise ValueError("mean: data must not be empty")
    return statistics.mean(seq)