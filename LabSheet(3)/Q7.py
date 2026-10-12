# 7. Reverse a string without using slicing

string = input("Enter a string: ")

reverse = ""

for char in string:
    reverse = char + reverse

print("Reversed string:", reverse)
