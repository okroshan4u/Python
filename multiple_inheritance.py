# Creat two calsses Battery and Engine and let the ElectricCar class inherit from both , demonstrating multiple inheritance 



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



class Battery:
    def battery_info(self):
        return "This is battery"
    
class Engine:
    def engine_info(self):
        return "This is Engine"  
    
class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
          