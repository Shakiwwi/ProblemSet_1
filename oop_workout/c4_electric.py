#No stretch


from c1_vehicle import Vehicle
 
 
class ElectricCar(Vehicle):
    def __init__(self, plate, make, model, year, battery_kwh, range_km):
        super().__init__(plate, make, model, year)
        self.battery_kwh = battery_kwh
        self.range_km = range_km
        self.__charge = 0.0
 
    def get_charge(self):
        return self.__charge
 
    def charge(self, kwh):
        if kwh <= 0:
            raise ValueError("kwh must be positive.")
        if self.__charge + kwh > self.battery_kwh:
            raise ValueError("Cannot charge past battery capacity.")
        self.__charge += kwh
 
    def drive(self, km):
        """use battery charge to drive km. Returns kWh consumed."""
        energy_needed = self.battery_kwh * km / self.range_km
        if energy_needed > self.__charge:
            raise ValueError("Not enough charge to drive that distance. Reduce Km.")
        self.__charge -= energy_needed
        super().drive(km)
        return energy_needed
 
    def describe(self):
        return f"{super().describe()}, electric car"