#Reverse a string using loops

str = "Roshan"
str2 = ""
# print(str[5])

# for c in range(len(str)):
#     l  = len(str) -1-c
#     str2= str2 + (str[l])
    
# print(str2)

# OR

for c in str:
    str2 = c + str2
    
print(str2)