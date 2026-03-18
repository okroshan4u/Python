# Find the first non-repeated characte
str = "rrosltot"

for char in str:
    if str.count(char) == 1:
        print(char)
        break
