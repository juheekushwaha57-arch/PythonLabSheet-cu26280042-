# 19. Write a program to remove duplicate elements from a tuple.
t = (1, 2, 2, 3, 4, 3, 5)
result = tuple(dict.fromkeys(t))
print("Tuple without duplicates:", result)
