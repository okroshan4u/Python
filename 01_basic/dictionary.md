>>> chai_types = {"Masala": "Spicy", "lemon": "sour","green":"Mild"}  
>>> chai_types
{'Masala': 'Spicy', 'lemon': 'sour', 'green': 'Mild'}
>>> for c in chai_types:
...     print(c)
>>>
...
Masala
lemon
green
>>> chai_types["Masala"]
'Spicy'
>>> chai_types.get("lemon")
'sour'
>>> chai_types.get("lemonn")
>>> chai_types["lemonn"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai_types["lemonn"]
    ~~~~~~~~~~^^^^^^^^^^
KeyError: 'lemonn'
>>> chai_types["lemonn"] = "nice"
>>> chai_types
{'Masala': 'Spicy', 'lemon': 'sour', 'green': 'Mild', 'lemonn': 'nice'}                                                                     }
>>>>>> for c in chai_types:
...     print(c , chai_types[c])
... 
Masala Spicy
lemon sour
green Mild
lemonn nice
>>>

>>> chai_types = {"Lemon": "Sour", "Earl Grey":"Mild","}
  File "<stdin>", line 1
    chai_types = {"Lemon": "Sour", "Earl Grey":"Mild","}
                                                      ^
SyntaxError: unterminated string literal (detected at line 1)
>>> chai_types = {"Lemon": "Sour", "Earl Grey":"Mild"}
>>> chai_types
{'Lemon': 'Sour', 'Earl Grey': 'Mild'}
>>> chai_types_copy = chai_types.copy()
>>> chai_types_copy
{'Lemon': 'Sour', 'Earl Grey': 'Mild'}
>>> del chai_types_copy
>>> chai_types_copy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai_types_copy
NameError: name 'chai_types_copy' is not defined
>>> tea_shop = {}
>>> tea_shop = {
... "chai":{"Masala":"Spicy", "Ginger":"Zesty"},
... "Tea":{"Green":"Mild","Black":"Strong"}
... }
>>> tea_shop
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}    
>>> tea_shop["chai"]
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> tea_shop["chai"]["Ginger"]
'Zesty'
>>>


>>> squared_num = {x:x**2 for x in range(6)}
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> print(squared_num)
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> squared_num.clear()
>>> squared_num
{}  
>>> keys = ["Masala", "Ginger","Lemon"]
>>> keys
['Masala', 'Ginger', 'Lemon']
>>> default_value = "Delicious"
>>> new_dict = dict.fromkeys(keys, default_values)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    new_dict = dict.fromkeys(keys, default_values)
                                   ^^^^^^^^^^^^^^
NameError: name 'default_values' is not defined. Did you mean: 'default_value'?
>>> new_dict = dict.fromkeys(keys, default_value)  
>>> new_dict
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
>>> new_dict = dict.fromkeys(keys, keys)
>>> new_dict
{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}
>>>
