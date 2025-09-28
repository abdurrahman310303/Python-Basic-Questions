from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
    
    def start_engine(self):
        return f"{self.make} car engine started"
    
    def stop_engine(self):
        return f"{self.make} car engine stopped"
    
    def honk(self):
        return "Beep beep!"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size
    
    def start_engine(self):
        return f"{self.make} motorcycle engine started"
    
    def stop_engine(self):
        return f"{self.make} motorcycle engine stopped"
    
    def wheelie(self):
        return "Performing wheelie!"

car = Car("Toyota", "Camry", 2023, 4)
motorcycle = Motorcycle("Honda", "CBR", 2023, "600cc")

vehicles = [car, motorcycle]

for vehicle in vehicles:
    print(vehicle.get_info())
    print(vehicle.start_engine())
    print(vehicle.stop_engine())
    print()

print(car.honk())
print(motorcycle.wheelie())
