from c1_vehicle import Vehicle
from c2_tank import FuelTank
 
 
class FuelledVehicle(Vehicle):
    def __init__(self, plate, make, model, year, capacity, consumption):
        super().__init__(plate, make, model, year)
        self.tank = FuelTank(capacity)
        self.consumption = consumption
 
    def refuel(self, litres):
        self.tank.fill(litres)
 
    def drive(self, km):
        """calculate fuel need for __km and call .consume from Fueltank class. returns litres used (fuel_needed)."""
        fuel_needed = self.consumption * km / 100
        self.tank.consume(fuel_needed)
        super().drive(km)
        return fuel_needed
 
    def range_remaining(self):
        return self.tank.get_level() / self.consumption * 100
 
 
class Car(FuelledVehicle):
    def __init__(self, plate, make, model, year, seats=5):
        super().__init__(plate, make, model, year, capacity=50.0, consumption=6.0)
        self.seats = seats
 
    def describe(self):
        return f"{super().describe()}, car, {self.seats} seats"
 
 
class Truck(FuelledVehicle):
    def __init__(self, plate, make, model, year, payload_kg):
        super().__init__(plate, make, model, year, capacity=200.0, consumption=18.0)
        self.payload_kg = payload_kg
 
    def describe(self):
        return f"{super().describe()}, truck, {self.payload_kg} kg payload"
 
 
class Motorcycle(FuelledVehicle):
    def __init__(self, plate, make, model, year):
        super().__init__(plate, make, model, year, capacity=15.0, consumption=3.5)
 
    def describe(self):
        return f"{super().describe()}, motorcycle"
 
 
class Van(FuelledVehicle):
    def __init__(self, plate, make, model, year, volume_m3):
        super().__init__(plate, make, model, year, capacity=75.0, consumption=9.0)
        self.volume_m3 = volume_m3
 
    def describe(self):
        return f"{super().describe()}, van, {self.volume_m3} m³"