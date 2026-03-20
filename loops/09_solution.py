# List the uniqueness checker
    # check if all the elements in the list aare uniue . if duplicate found , xit the loop and print the duplicate
    
items = ["Apple","Banana","Grapes","Apple","Mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate item :",item) 
        break
    unique_item.add(item)
print(unique_item)    