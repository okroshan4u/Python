# Write a functin named multiply that multiplies tow numbers, but can also accepts and mulitply strings

# def multiply(p1, p2): # here it not sutitable for the string 
#     return p1 * p2


def multiply(p1, p2):
    if isinstance(p1, str) and isinstance(p2, str): # if p1 is a string AND p2 is also a string then.....
        return p1 + p2
    return p1 * p2


print(multiply(4,6))
print(multiply("r",6))
print(multiply(4,"h"))
print(multiply("r","h"))
