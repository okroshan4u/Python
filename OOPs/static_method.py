# Add a static method to the car class that returns a general description of a car

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
    @staticmethod  # here staticmetod is called the decorators 
    def general_description():
        return "Cars are means of transport and are amazing"
    
    
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

# print(my_car.general_description())
print(my_car.general_description())

# print(Car.total_car)      