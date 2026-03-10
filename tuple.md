<!-- tuple are immutable in python -->

>>> chai_types = ("Lemon","Black","Green")
>>> chai_types
('Lemon', 'Black', 'Green')
>>> chai_types[0]
'Lemon'
>>> chai_types[:2]
('Lemon', 'Black')
>>> chai_types[1:] 
('Black', 'Green')
>>> len(chai_types)
3   
>>> more_tea = ("Herbal", "Earl Grey")
>>> all_tea = more_tea + tea_types
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    all_tea = more_tea + tea_types
                         ^^^^^^^^^
NameError: name 'tea_types' is not defined. Did you mean: 'chai_types'?
>>> all_tea = more_tea + chai_types
>>> all_tea
('Herbal', 'Earl Grey', 'Lemon', 'Black', 'Green')
>>> if "Green" in all_tea:
...     print("I have green tea")
... 
I have green tea
>>> more_tea
('Herbal', 'Earl Grey')
>>> more_tea = ("Herbal",Earl Grey","Herbla")
  File "<stdin>", line 1
    more_tea = ("Herbal",Earl Grey","Herbla")
                         ^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> more_tea = ("Herbal","Earl Grey","Herbla")
>>> more_tea.count("Herbal")
1
>>> more_tea = ("Herbal","Earl Grey","Herbal") 
>>> more_tea
('Herbal', 'Earl Grey', 'Herbal')
>>> more_tea.count("Herbal")
2
>>> more_tea.count("herb")
0
>>> chai_types
('Lemon', 'Black', 'Green')
>>>  (lemon,black,greeen) = chai_types
  File "<stdin>", line 1
    (lemon,black,greeen) = chai_types
IndentationError: unexpected indent
>>>  (lemon, black, green) = chai_types 
  File "<stdin>", line 1
    (lemon, black, green) = chai_types
IndentationError: unexpected indent
>>> chai_types
('Lemon', 'Black', 'Green')
>>> (lemon, black, green) = chai_types  
>>> lemon
'Lemon'
>>> type(chai_types)
<class 'tuple'>

>>>

