class Vehicle:
    fleet_size = 0

    def __init__(self, plate, make, model, year):
        self.plate = plate
        self.make = make
        self.model = model
        self.year = year
        self.kilometres = 0
        Vehicle.fleet_size += 1

    def drive(self, km):
        """adds to self.kilometers and raises and error in incorrect input: 0 or negative values."""
        if km <= 0:
            raise ValueError("No km to add. Pls enter positive value.")
        self.kilometres += km

    def describe(self):
        return f"{self.year} {self.make} {self.model} {self.plate}"

    def service_due(self):
        """True if condition below is met"""
        return self.kilometres > 15000

    def __str__(self):
        return self.describe()

    def __repr__(self):
        return type(self).__name__ + "('" + self.plate + "', '" + self.make + "', '" + self.model + "', " + str(self.year) + ")"

    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            return False
        return self.plate == other.plate

    def __hash__(self):
        return hash(self.plate)

    def __lt__(self, other):
        return self.plate < other.plate
