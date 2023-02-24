

class Transport:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def message (self):
        print(f'{self.brand} {self.model} has max speed {self.max_speed} km/h')


class Car(Transport):
    def __init__(self, brand, model, max_speed):
        super().__init__(brand, model)
        self.max_speed = max_speed

car = Car('Mazda','6', 222)
car.message()


class Plane(Transport):
    def __init__(self, brand, model, max_altitude):
        super().__init__(brand, model)
        self.max_altitude = max_altitude

    def message(self):
        print(f'{self.brand} {self.model} has maximum altitude {self.max_altitude} m')

plane = Plane('Airbus', 'A-320', 15000)
plane.message()


class Ship(Transport):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def message(self):
        print(f'The cruise ship {self.brand} {self.model} can carry {self.capacity} passengers')


ship = Ship('STX France', '\'Harmony of the Seas\'', 6500)
ship.message()

