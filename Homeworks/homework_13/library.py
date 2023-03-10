from abc import ABC, abstractmethod


class Gadget(ABC):
    def __init__(self, brand: str, model: str, price: int, country: str):
        self.brand = brand.upper()
        self.model = model.upper()
        self.price = price
        self.country = country

    def __str__(self):
        return f'Gadget {self.brand} {self.model} has price {self.price} $'

    @abstractmethod
    def get_additional_info(self):
        pass

    @property
    def country_of_production(self):
        return self.country


class Phone(Gadget):
    def __init__(self, brand: str, model: str, price: int, country: str, battery_capacity: int):
        super().__init__(brand=brand, model=model, price=price, country=country)
        self.battery_capacity = battery_capacity

    def get_additional_info(self):
        return f'This phone has {self.battery_capacity} mA/h capacity'


class Laptop(Gadget):
    def __init__(self, brand: str, model: str, price: int, country: str, screen_refresh_rate: int):
        super().__init__(brand=brand, model=model, price=price, country=country)
        self.screen_refresh_rate = screen_refresh_rate

    def get_additional_info(self):
        return f'Refresh screen rate of this laptop is {self.screen_refresh_rate}'


