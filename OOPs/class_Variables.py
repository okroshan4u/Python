# Add a class variable to Car that keeps track of the number of cars crea
class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model
        Car.total_car += 1
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


# my_ele_car = ElectricCar("Tesla", "Model S", "85kwh")
# print(my_ele_car.brand)      
# print(my_ele_car.model)      
# print(my_ele_car.batterSize)      
# print(my_ele_car.fuel_type())

my_car = Car("Toyota", "Corolla")
my_new_car = Car("Maruti Suzuki", "800")
my_new_car_new = Car("Maruti Suzuki", "800")

print(Car.total_car)      
