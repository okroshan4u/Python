# Demonstrate polymorphism by defining a method fuel_type in both Car and ElelctricCar calsses but with defferent behaviours 


class Car:
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model
    def fuel_type(self):
        return "Petrol and Diesel"    
    def fullname(self):
        return f"{self.brand} {self.model}"    
    
    
class ElectricCar(Car):
    
    def __init__(self,brand, model, batterySize):
        super().__init__(brand , model)
        self.batterSize = batterySize
    def fuel_type(self):
        return "Electric Charge" 


my_ele_car = ElectricCar("Tesla", "Model S", "85kwh")
print(my_ele_car.brand)      
print(my_ele_car.model)      
print(my_ele_car.batterSize)      
print(my_ele_car.fuel_type())      