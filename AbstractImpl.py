from abc import *
class Vehicle(ABC):
    @abstractmethod
    def noofwheels(self):
        pass

class Bus(Vehicle):
    def noofwheels(self):
        return 7

class Auto(Vehicle):
    def noofwheels(self):
        return 3
b=Bus()
print(b.noofwheels())#7

a=Auto()
print(Auto().noofwheels())#3