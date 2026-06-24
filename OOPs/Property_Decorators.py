# Use a property decorator in the Car class to make the model attribute read-on

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
    
    @staticmethod
    def general_description():
        return "This is general description"    
    @property        # if prevents of changing anything to the model
    def model(self):
        return self.__model
    
my_car = Car("Toyota", "Corola")

# my_car.model = "City" # since property decorator is applied on the model by making it private so it can not be changed here


print(my_car.model)  # so the property decorator made it accessible like the propery of the class Car

# print(my_car.general_description())
