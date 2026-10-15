# 22. Write a program to flatten a nested tuple.
t = ((1, 2), (3, 4), (5, 6))
result = tuple(item for sub in t for item in sub)
print("Flattened tuple:", result)
