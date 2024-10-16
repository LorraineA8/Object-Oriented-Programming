from Garage_class import Garage

from Truck_class import Truck

class GarageTester(Garage):
    def __init__(self):
        super().__init__()
        
    def getExample(self):
        truck = Truck("black", False)
        garage = Garage()
        garage.setVehicle(truck)
        return garage.toString()
        
if __name__ == '__main__':
    print(GarageTester().getExample())