# 29. Write a program to check if all elements in a tuple are the same.
t = (5, 5, 5, 5, 5)

if len(set(t)) == 1:
    print("All elements are the same")
else:
    print("All elements are not the same")
