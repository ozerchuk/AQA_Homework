import pytest


@pytest.fixture(scope='function', autouse=True)
def package_fixture3():
    print('\nStarting')
    yield
    print('\nFinishing')
