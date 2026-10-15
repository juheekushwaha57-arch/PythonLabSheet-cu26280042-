# 30. Write a program to find the element-wise sum of two tuples.
t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)

result = tuple(a + b for a, b in zip(t1, t2))
print("Element-wise sum:", result)
