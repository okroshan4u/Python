#prime number checker

num = int(input("Enter a number to check for prime : "))

# for i in range(num-1):
#     print(i+1)
#     if(num % (i+1) != 0):
#         print("Your number is prime: ", num)
#         break
is_Prime = True

if num > 1:
    for i in range(2, num):
        if (num % i ) == 0:
            is_Prime = False
            break
print(is_Prime)    