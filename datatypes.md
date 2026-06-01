<!-- >>> h1 = [1,2,3]
>>> h1
[1, 2, 3]
>>> h2 = h1[:] ## when we are slicing then we are making the copy of the h1 that means a new reference to the h2 so anything change in h1 will not change h2
>>> h2
[1, 2, 3]
>>> h1[0] = 25
>>> h1
[25, 2, 3]
>>> h2
[1, 2, 3]
>>>   

>>> import copy
>>> h2 = copy.copy(h1)
>>> h2 = copy.deepcopy(h1) -->

>>> m = [1,2,3]
>>> n = m 
>>> m
[1, 2, 3]
>>> n    
[1, 2, 3]
>>> m = n
>>> m == n  // while here it is checking the value only no the reference in the memory
True
>>> m === n
  File "<stdin>", line 1
    m === n
        ^
SyntaxError: invalid syntax
>>> n = [1,2,3]
>>> m == n
True
>>> m is n  // here "is" operator checks  the reference in the memory is same or not 

False


