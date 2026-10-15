# 18. Write a program to remove all elements of one set from another set.
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5}
s1.difference_update(s2)
print("Result:", s1)
