import random
import string


def generate_random_number() -> int:
    """
    Generates a random int number between -10^10 and 10^10
    """
    return random.randint(-10**10, 10**10)


def generate_random_string(length: int = 10) -> str:
    """
    Generates a random string of given length with lowercase English alphabet
    """
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))




