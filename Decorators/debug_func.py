# Debugging function calls
# Create a decorator to print the function name and the values of its arguments every time the function is calle

import time

def debug(func):
    def wrapper(*args , **kwargs):
        
        result = func(*args, **kwargs)
        
        arg_value = ', '.join(str(arg) for arg in args)
        
        kwarg_value = ', '.join(f"{k} - {v}" for k , v in kwargs.items())
        
        print(f"calling : {func.__name__} with args {arg_value} and kwarg {kwarg_value}")
        return result
    return wrapper    
        
@debug
def greet(name , greeting = "Hello"):
    print(f"{name} - {greeting}")
    

    
greet("Chai" , greeting="hello") 





