# Find the first non-repeated character
# loops in handy
str = "rrosltot"

for char in str:
    if str.count(char) == 1:
        print(char)
        break
