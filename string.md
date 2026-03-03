In python we represent string with '',"", """ """ that is with single quotation , double quotation and triple quotation

>>> name = 'Roshan Kumar Ram'
>>> name
'Roshan Kumar Ram'
>>> first_char = name[0]
>>> print(first_char)
R   
>>> first_name = name[0:6]
>>> print(first_name]
  File "<stdin>", line 1
    print(first_name]
                    ^
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> print(first_name)
Roshan
>>> num_list = "0123456789"
>>> num_list
'0123456789'
>>> print(num_list)
0123456789
>>> num_list[0:]
'0123456789'
>>> num_list[3:] 
'3456789'
>>> num_list[:7] 
'0123456'
>>> num_list[0:7:2]  <!--- skipping 1 char --->
'0246'
>>> num_list[0:7:1]  <!--- skipping 0 char --->
'0123456'
>>> num_list[0:7:3]  <!--- skipping 2 char starting from 0 --->
'036'
>>>



>>> name
'Roshan Kumar Ram'
>>> name.lower()
'roshan kumar ram'
>>> name.upper()
'ROSHAN KUMAR RAM'
>>> name2 = "  Roshan  "
>>> name2
'  Roshan  '
>>> name2.stripe()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name2.stripe()
    ^^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'stripe'. Did you mean: 'strip'?
>>> name2.strip()  
'Roshan


>>> name = "Roshan Kumar Ram"
>>> name
'Roshan Kumar Ram'
>>> name.find("Ram")
13
>>> name.find("ram")
-1
>>>

<!-- From string  to split  -->
>>> name = "Roshan, Ram, Rahul, Jenny"
>>> name
'Roshan, Ram, Rahul, Jenny'
>>> name.split()
['Roshan,', 'Ram,', 'Rahul,', 'Jenny']
>>> name.split(", ")
['Roshan', 'Ram', 'Rahul', 'Jenny']

<!-- From list to string  -->
>>> name_variety = ["Roshan", "Neha", "Jenny", "Sweta","Marcos"]
>>> name_variety
['Roshan', 'Neha', 'Jenny', 'Sweta', 'Marcos']
>>> print("".join(name_variety)
... 
... 
... ^D
  File "<stdin>", line 4
    ♦
    ^
SyntaxError: invalid non-printable character U+0004
>>> print("".join(name_variety))
RoshanNehaJennySwetaMarcos
>>> print(" ".join(nme_variety))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(" ".join(nme_variety))
                   ^^^^^^^^^^^
NameError: name 'nme_variety' is not defined. Did you mean: 'name_variety'?
>>> print(" ".join("name_variety))
  File "<stdin>", line 1
    print(" ".join("name_variety))
                   ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print(" ".join(name_variety))
Roshan Neha Jenny Sweta Marcos
>>> print(", ".join(name_variety))
Roshan, Neha, Jenny, Sweta, Marcos
>>> print("-".join(name_variety))
Roshan-Neha-Jenny-Sweta-Marcos
>>>   





>>> name = "Roshan kumar  Ram"
>>> name.count("R")
2
>>> chai_type = "Masala"
>>> quantity = 2
>>> order = "I ordered {} cups of {} chai" 
>>> order 
'I ordered {} cups of {} chai'              <!-- ihere {} known as placeholders where we can put variables using format method--->
>>> print(order.format(quantity, chai_type))
I ordered 2 cups of Masala chai
>>>


<!-- writing quotations and paths with raw -->
>>> quote = "Ram  is "good" boy "
  File "<stdin>", line 1
    quote = "Ram  is "good" boy "
                      ^^^^
SyntaxError: invalid syntax. Is this intended to be part of the string?
>>> quote = "Ram  is \"good\" boy " 
>>> quote
'Ram  is "good" boy '
>>> chai = "masala\nchai"
>>> chai
'masala\nchai'
>>> chai = r"masala\nchai"
>>> chai
'masala\\nchai'
>>> print(chai)
masala\nchai
>>> path = "c:\user\windows\"
  File "<stdin>", line 1
    path = "c:\user\windows\"
           ^
SyntaxError: unterminated string literal (detected at line 1); perhaps you escaped the end quote?
>>> path = "c:\user\windows"  
  File "<stdin>", line 1
    path = "c:\user\windows"
           ^^^^^^^^^^^^^^^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
>>> path = r"c:\user\windows\" 
  File "<stdin>", line 1
    path = r"c:\user\windows\"   <!-- here r represetns raw just like javascript-->
           ^
SyntaxError: unterminated string literal (detected at line 1); perhaps you escaped the end quote?
>>> path = r"c:\user\windows"  
>>> print(path)
c:\user\windows
>>>
>>> path = "c:\\users\\windows" 
>>> print(path)
c:\users\windows
>>>

'Roshan kumar  Ram'
>>> print("kumar" in name)
True
>>> print("Kumar" in name)
False
>>>  

