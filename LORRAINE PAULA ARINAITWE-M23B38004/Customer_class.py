class Customer:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        
    def toString(self):
        return f'Customer Information: \nName: {self.name}\nAddress: {self.address}'


if __name__ == '__main__':
    #Customer class object
    customer1 = Customer('ARINAITWE', 'MUKONO')
    #Customer information
    print(customer1.toString())