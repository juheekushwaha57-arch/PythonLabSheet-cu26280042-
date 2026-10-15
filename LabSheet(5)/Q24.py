# 24. Write a program to find common elements between two tuples.
t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)

common = tuple(x for x in t1 if x in t2)
print("Common elements:", common)
