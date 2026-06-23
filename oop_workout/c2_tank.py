class FuelTank:

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Pls input positive value for capacity.")
        self.__capacity = capacity
        self.__level = 0.0
 
    def get_level(self) -> float:
        return round(self.__level, 2)
 
    def get_capacity(self) -> float:
        return self.__capacity
 
    def fill(self, litres):
        """adds input to self.litres. value errors if  0 or negative value(litres) and if self.capacity is exceeded value."""
        if litres <= 0:
            raise ValueError()
        if self.__level + litres > self.__capacity:
            raise ValueError()
        self.__level += litres
 
    def consume(self, litres):
        """subrtracts input from self.level, value error if input 0 or less and if greater than seld.level"""
        if litres <= 0:
            raise ValueError("Litres must be positive.")
        if litres > self.__level:
            raise ValueError("Not enough fuel left to consume. Reduce litres.")
        self.__level -= litres
        
    def fill_to_full(self) -> float:
        """makes self.level into self.capacity (filling to tank to full). returns the difference (litres_added)"""
        litres_added = self.__capacity - self.__level
        self.__level = self.__capacity
        return litres_added
    
    def percent_full(self):
        return round((self.__level / self.__capacity) * 100, 1)



