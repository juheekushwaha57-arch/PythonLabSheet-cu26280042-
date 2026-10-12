
# 4. Extract all uppercase characters from a string

string = input("Enter a string: ")

uppercase = ""

for char in string:
    if char.isupper():
        uppercase += char

print("Uppercase characters:", uppercase)
