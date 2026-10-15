# 25. Write a program to find the difference between two tuples.
t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)

difference = tuple(x for x in t1 if x not in t2)
print("Difference:", difference)
