# Write a decorator that measures the time a function takes to execu
import time 


def calctime(func):
    def wrapper(*args , **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
        
    return wrapper    



@calctime
def example_function(n):
    time.sleep(n)
    
example_function(2)  
    
