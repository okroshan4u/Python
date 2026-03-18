# Find factorial of a number using while

num = int(input("Enter the number of which you want factorial: "))
fact = 1;
while (num >0):
    fact = fact * num
    num = num -1
    
print(fact)    