import pytest
import lib


def test1() -> None:
    """
    Checking whether a function returns a string
    """
    assert isinstance(lib.generate_random_string(), str)


def test2() -> None:
    """
    Check that the generate_random_string function works with parameter 20
    """
    assert isinstance(lib.generate_random_string(20), str)


def test3() -> None:
    """
    Check that the generate_random_string function works with parameter -1
    """
    assert isinstance(lib.generate_random_string(-1), str)


def test4() -> None:
    """
    Check that the generate_random_string function works with parameter 5.5
    """
    assert isinstance(lib.generate_random_string(5.5), str)


def test5() -> None:
    """
    Check that the generate_random_string function works with parameter 5.5
    """
    assert len(lib.generate_random_string(0)) == 0


def test6() -> None:
    """
    Check that the generate_random_string function works with parameter 5.5
    """
    assert len(lib.generate_random_string(1)) == 1





