# 27. Write a program to check if two strings are anagrams using sets.
str1 = "listen"
str2 = "silent"

if len(str1) == len(str2) and set(str1) == set(str2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")
    
