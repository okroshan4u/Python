# Debugging function calls
# Create a decorator to print the function name and the values of its arguments every time the function is called

import time

def debug(func):
    def wrapper(*args , **kwargs):
        
        result = func(*args, **kwargs)
        arg_value = 
        print(f"{func.__name__} is taking")
        return result
    return wrapper    
        

def greet(name , greeting = "Hello"):
    print(f"{name} - {greeting}")
    

    
greet("Chai" , greeting="hello") 





