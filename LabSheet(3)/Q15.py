
# 15. Find the first non-repeated character in a string

text = input("Enter a string: ")

for char in text:
    if text.count(char) == 1:
        print("First non-repeated character:", char)
        break
else:
    print("No non-repeated character found")
