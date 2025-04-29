class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

class ElectricCar(Car):
    def __init__(self, brand, color, battery_size):
        super().__init__(brand, color)

        self.battery_size = battery_size