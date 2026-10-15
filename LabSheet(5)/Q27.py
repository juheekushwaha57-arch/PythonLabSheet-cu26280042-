# 27. Write a program to unzip a list of tuples into individual lists.
t = [(1, 'a'), (2, 'b'), (3, 'c')]

numbers, letters = zip(*t)

print("Numbers:", list(numbers))
print("Letters:", list(letters))
