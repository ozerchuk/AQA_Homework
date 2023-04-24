import pytest


@pytest.fixture(scope='session', autouse=True)
def package_fixture1():
    print('\nStarting pack')
    yield
    print('\nFinishing pack')