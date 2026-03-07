>>> chai_varieties = ["Oolong", "lemon", "Green","red"]
>>> chai_varieties
['Oolong', 'lemon', 'Green', 'red']
>>> print(chai_varieties)
['Oolong', 'lemon', 'Green', 'red']
>>> print(chai_varieties[0])
Oolong
>>> print(chai_varieties[2]) 
Green
>>> print(chai_varieties[-1])
r
>>> print(chai_varieties[:2]) 
['Oolong', 'lemon']
>>> print(chai_varieties[1:]) 
['lemon', 'Green', 'red']
>>> chai_varieties[2] = "White"        
>>> print(chai_varieties)
['Oolong', 'lemon', 'White', 'red']
>>> for c in chai_varieties:
...     print(c)
... 
Oolong
lemon 
White 
red   
>>>


>>> chai_varieties = ["Oolong", "Lemon","Green","Black"]
>>> chai_varieties
['Oolong', 'Lemon', 'Green', 'Black']
>>> chai_varieties[1] = "Herbal"
>>> chai_varieties               
['Oolong', 'Herbal', 'Green', 'Black']
>>> chai_varieties                                       
['Oolong', 'Herbal', 'Green', 'Black']
>>> chai_varieties[:2]
['Oolong', 'Herbal']
>>> chai_varieties[1:4] 
['Herbal', 'Green', 'Black']
>>> chai_varieties[1:]  
['Herbal', 'Green', 'Black']
>>> chai_varieties[1:2]="White"
>>> chai_varieties             
['Oolong', 'W', 'h', 'i', 't', 'e', 'Green', 'Black']
>>> chai_varieties = ["Oolong", "Lemon","Green","Black"]
>>> chai_varieties[1:2] = ["White"]                      
>>> chai_varieties
['Oolong', 'White', 'Green', 'Black']
>>> 

>>> chai_varieties[1:1]
[]  
>>> chai_varieties[1:1]= ["test", "test"]
>>> chai_varieties                        
['Oolong', 'test', 'test', 'White', 'Green', 'Black']
>>> chai_varieties[1:2]
['test']
>>> chai_varieties[1:3] 
['test', 'test']
>>> chai_varieties[1:3] = []   <!--- insert nothing operation or delete operation --->
>>> chai_varieties          
['Oolong', 'White', 'Green', 'Black']
>>>

>>> for c in chai_varieties:
...     print(c)
... 
Oolong
White 
Green 
Black 
>>> for c in chai_varieties:
...     print(c, end="-")
... 
Oolong-White-Green-Black->>> 

['Oolong', 'White', 'Green', 'Black', 'Red']
>>> if "Red" in chai_varieties:
...     print("I have Red tea")
... 
I have Red tea
>>> chai_varieties.pop()
'Red'
>>> chai_varieties
['Oolong', 'White', 'Green', 'Black']
>>> chai_varieties.pull()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai_varieties.pull()
    ^^^^^^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'pull'
>>> chai_varieties.remove("Green")
>>> chai_varieties
['Oolong', 'White', 'Black']
>>>

>>> range(10)
range(0, 10)
>>> print(range(10))
range(0, 10)
>>> y = range(10)
>>> y
range(0, 10)
>>> squared_num = [x**2 for x in range(10)]
>>> squared_num
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  File "<stdin>", line 1
    cube_num = [y**3 for y in range(5)]
IndentationError: unexpected indent
>>> cobe_num = [ y**3 for y in range(5)]
>>> cobe_num

[0, 1, 8, 27, 64]
