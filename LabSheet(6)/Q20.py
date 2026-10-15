# 20. Write a program to find the Cartesian product of two sets.
s1 = {1, 2}
s2 = {'a', 'b'}
product = {(x, y) for x in s1 for y in s2}
print("Cartesian product:", product)
