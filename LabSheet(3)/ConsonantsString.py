# 2. Count the number of vowels and consonants in a string

string = input("Enter a string: ")

vowels = 0
consonants = 0

for char in string.lower():
    if char in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
