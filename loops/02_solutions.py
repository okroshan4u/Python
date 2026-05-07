# print the number in the range given by user and add the even number amoung the

sum = 0

num = int(input("Enter your num upto which you want the sum of even number: "))

print("The number you entered is : ",num)


for i in range(num):
    print(f"The numbers from 1 to {num} are : ",i+1)
    if(i+1) % 2 == 0:
        sum = sum + (i+1)
print(f"The sum of the even numbers from 1 to {num} is : ",sum)        
