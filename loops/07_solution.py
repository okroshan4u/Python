#Keep asking the user for input untill they enter a number between 1 and 10


while(True):
    # print("Enter the number : ")
    num = int(input("Enter the number : "))
    if(num >=1 and num <= 10):
        print("Your number is ", num)
        break   