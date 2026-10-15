# 20. Write a program to find the length of the longest word in a tuple.
t = ("apple", "banana", "watermelon", "mango")
length = max(len(word) for word in t)
print("Length of longest word:", length)

