#no stretch

class Fleet:
    def __init__(self, name):
        self.name = name
        self._vehicles = {}

    def add(self, vehicle):
        """if a vehicle with the same plate exists, raise an error"""
        if vehicle.plate in self._vehicles:
            raise ValueError("Vehicle with same plate is already in fleet.")
        self._vehicles[vehicle.plate] = vehicle

    def remove(self, plate):
        """if the plate is not in the fleet, raise an error"""
        if plate not in self._vehicles:
            raise KeyError(plate)
        del self._vehicles[plate]

    def find(self, plate):
        return self._vehicles.get(plate)

    def total_kilometres(self):
        """add up the kilometres of every vehicle in fleet"""
        total = 0
        for vehicle in self._vehicles.values():
            total += vehicle.kilometres
        return total

    def drive_all(self, km):
        """try to drive every vehicle, collect the ones that worked and the ones that failed"""
        successes = []
        failures = []
        for plate, vehicle in self._vehicles.items():
            try:
                vehicle.drive(km)
                successes.append(plate)
            except Exception as e:
                failures.append((plate, str(e)))
        return successes, failures

    def __len__(self):
        return len(self._vehicles)

    def __iter__(self):
        return iter(self._vehicles.values())

    def __contains__(self, plate):
        return plate in self._vehicles

    def __str__(self):
        return "Fleet '" + self.name + "': " + str(len(self)) + " vehicle(s)"


def print_summary(fleet):
    """print a full report of the fleet and all its vehicles"""
    print("=== FLEET REPORT ===")
    print(fleet)
    print("Total kilometres: " + str(fleet.total_kilometres()))
    print("--------------------")
    for vehicle in fleet:
        print(vehicle)
    print("====================")



    