# 11. Check if two strings are anagrams of each other

str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()

if sorted(str1.replace(" ", "")) == sorted(str2.replace(" ", "")):
    print("Anagrams")
else:
    print("Not Anagrams")
    
