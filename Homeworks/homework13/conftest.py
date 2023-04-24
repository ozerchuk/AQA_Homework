import pytest
from library import Phone
from library import Laptop


@pytest.fixture(scope='class')
def phone():
    phone_data = Phone(
        brand='Apple',
        model='12 Pro',
        price=1000,
        country='USA',
        battery_capacity=2800
    )
    yield phone_data


@pytest.fixture(scope='class')
def laptop():
    laptop_data = Laptop(
        brand='Asus',
        model='Zenbook',
        price=1200,
        country='Taiwan',
        screen_refresh_rate=120
     )
    yield laptop_data
