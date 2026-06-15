# Modify the Car calss to encapsulate the brand attribute, making it private, making it private , and povide a getter method for it

class Car:
    def __init__(self, brand, model):
        self.__brand = brand   # here we are making the brand private by just two underscore
        self.model = model
        
    def fullname(self):
        return f"{self.__brand} {self.model}" 
    
    def get_brand(self):
        return self.__brand + "!"
    
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterSize = batterySize
        
my_ele_car = ElectricCar("Tesla", "Model S", "85kwh")
print(my_ele_car.get_brand())      
print(my_ele_car.model)      
print(my_ele_car.batterSize)      
print(my_ele_car.fullname())          
                   