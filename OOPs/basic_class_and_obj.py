# Create a Car class with attributes like brand and model. Then create an instance of this calss

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
     
     
my_car = Car("Corolla","Toyota")


print(my_car.brand)      
print(my_car.model)      