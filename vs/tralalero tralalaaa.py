from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def move (self):
        pass

class Car(vehicle):
    def move(self):
        print("manqana mozraobs")

class Bicycle(vehicle):
    def move(self):
        print("velosipedi mozraobs")


vehicle1 = Car()
vehicle2 = Bicycle()

vehicle1.move()
vehicle2.move()