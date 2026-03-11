<!-- basi operators are there -->

>>> import math
>>> math.floor(3.6)
3   
>>> math.floor(-3.5)
-4  
>>> math.floor(3.9)
3   
>>> math.trunc(2.8)
2   
>>> math.trunc(-2.8)   <!--- trunc takes the number towards zero --->
-2  
>>> 

<!-- octal , hexal and binary conversion -->
>>> 0o20
16  
>>> 0xFF
255 
>>> 0b1000
8   
>>> oct(64)
'0o100'
>>> hex(64)
'0x40'
>>> bin(64)
'0b1000000'
>>>

>>> int('64', 8)
52
>>> int('64', 16)
100
>>> int('64', 2)  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    int('64', 2)
    ~~~^^^^^^^^^
ValueError: invalid literal for int() with base 2: '64'
>>> int('1000', 2)
8
>>>

<!-- random method-->

>>> import random
>>> random.random()
0.8458734659979511
>>> random.random()
0.7038406138706013
>>> random.randint(1,100)
58
>>> random.randint(1,100)
5
>>> random.randint(1,100)
51
>>> random.randint(20,30)  <!-- here last number not inclusive just like most  languages  -->
20
>>> random.randint(20,30)
27
>>> random.randint(20,30)
25
>>>

'ginger'
>>> l1
['lemon', 'masala', 'ginger', 'mint']
>>> random.choice(l1)
'lemon'
>>> random.choice(l1)
'ginger'
>>> random.choice(l1)
'mint'
>>> random.suffle(l1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    random.suffle(l1)
    ^^^^^^^^^^^^^
AttributeError: module 'random' has no attribute 'suffle'. Did you mean: 'shuffle'?
>>> random.shuffle(l1)
>>> l1                 
['mint', 'masala', 'lemon', 'ginger']
>>> random.choice(l1)
'masala'
>>> random.shuffle(l1)
>>> l1                 
['masala', 'lemon', 'ginger', 'mint']
>>> random.shuffle(l1)
>>> l1                 
['masala', 'ginger', 'mint', 'lemon']
>>>


>>> 0.1+0.1+0.2
0.4
>>> 0.1 + 0.1+ 0.1
0.30000000000000004
>>> 0.1 + 0.1+ 0.1 - 0.3 
5.551115123125783e-17
>>> from decimal import decimal
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    from decimal import decimal
ImportError: cannot import name 'decimal' from 'decimal' (C:\Users\lenovo\AppData\Local\Programs\Python\Python314\Lib\decimal.py). Did you mean: 'Decimal'?
>>> from decimal import Decimal 
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
Decimal('0.3')
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')
>>> from fractions import Fraction 
>>> myFra = Fraction(3,8)
>>> myFra
Fraction(3, 8)

>>>

