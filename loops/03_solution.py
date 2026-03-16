# print the multiplication table of the given number and skips the 5th interation
num = int(input(print("Enter the number you want table of : ")))

for n in range(10):
    if (n + 1) == 5:
         continue           # continue skips the iteration 
    print(f"{num} * {n+1} = ",(n+1)*num)