# Base class: Vehicle
class Vehicle:
    def __init__(self, name, max_speed, capacity):
        self.name = name
        self.max_speed = max_speed
        self.capacity = capacity
    
    def details(self):
        return f"{self.name}: Max Speed = {self.max_speed} km/h, Capacity = {self.capacity} passengers"

# child class: Car
class Car(Vehicle):
    def __init__(self, name, max_speed, capacity, fuel_type):
        super().__init__(name, max_speed, capacity)
        self.fuel_type = fuel_type

    def details(self):
        return super().details() + f", Fuel Type = {self.fuel_type}"

# child2 class: ElectricCar
class ElectricCar(Car):
    def __init__(self, name, max_speed, capacity, battery_capacity):
        super().__init__(name, max_speed, capacity, fuel_type="Electric")
        self.battery_capacity = battery_capacity

    def details(self):
        return super().details() + f", Battery Capacity = {self.battery_capacity} kWh"

# Testing the classes
vehicle = Vehicle("Generic Vehicle", 120, 5)
car = Car("Sedan", 180, 4, "Petrol")
electric_car = ElectricCar("Tesla Model 3", 200, 4, 75)

print(vehicle.details())
print(car.details())
print(electric_car.details())


# Activity 2: Polymorphism Challenge

# Base class: Vehicle
class Vehicle:
    def move(self):
        return "Moving in an undefined way..."

# child1 class: Car
class Car(Vehicle):
    def move(self):
        return "Driving"

# child2 class: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying"

# child3 class: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing"

# Polymorphism demonstration
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())

