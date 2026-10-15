# 22. Write a program to find duplicate elements in a list using a set.
lst = [1, 2, 3, 2, 4, 1, 5, 3]
seen = set()
duplicates = set()

for item in lst:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print("Duplicate elements:", duplicates)

