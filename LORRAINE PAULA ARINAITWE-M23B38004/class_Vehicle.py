class Vehicle:
    def __init__(self, color):
        self.color = color
        
        
    def getColor(self):
        return f"{self.color}"
        
    def toString(self):
        return f"The color of the vehicle is {self.getColor()}"
    
if __name__ == '__main__':      
        
    vehicle1 = Vehicle("red")
    vehicle1.getColor()
    vehicle1.toString()


    print(vehicle1.getColor())
    print(vehicle1.toString())


    
    
