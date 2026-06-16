# Create and ElectricCar calss that inherits from the Car class and has and additional attribute battery_size

class Car:
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model
        
    def fullname(self):
        return f"{self.brand} {self.model}"    
    
    
class ElectricCar(Car):
    
    def __init__(self,brand, model, batterySize):
        super().__init__(brand , model)
        self.batterSize = batterySize
    
    
# mycar = Car("Toyota","Corolla")
# print(mycar.brand)        
# print(mycar.model)        
# print(mycar.fullname())  

my_ele_car = ElectricCar("Tesla", "Model S", "85kwh")
print(my_ele_car.brand)      
print(my_ele_car.model)      
print(my_ele_car.batterSize)      
print(my_ele_car.fullname())      