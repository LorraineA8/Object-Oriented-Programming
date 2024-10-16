class Garage:
    def __init__(self):
        self.Vehicle = None

    def setVehicle(self, parked_vehicle):
        self.Vehicle = parked_vehicle
        return f"The parked car is {self.setVehicle}"
    
    def toString(self):
        return f"Description of the parked vehicle:\n {self.Vehicle.toString()}"
    
        
    
        

    