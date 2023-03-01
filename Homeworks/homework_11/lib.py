import random
import string
from typing import Union


def generate_random_number() -> float:
    """
    Generates a random float number between -10^10 and 10^10
    """
    return random.uniform(-10**10, 10**10)


def generate_random_string(length: Union[int, float] = 10) -> str:
    """
    Generates a random string of given length with lowercase English alphabet
    """
    # check for float numbers and convert them to an integer type
    if not isinstance(length, int):
        length = int(length)
    # length cannot be less than zero
    length = max(length, 0)
    # string generation
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))




