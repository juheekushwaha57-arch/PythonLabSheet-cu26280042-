# 22. Create a dictionary with numbers as keys and their squares as values

n = int(input("Enter n: "))

squares = {}

for i in range(1, n + 1):
    squares[i] = i * i

print("Dictionary:", squares)

