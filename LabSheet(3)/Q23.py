
# 23. Remove duplicate elements from a list

numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("List without duplicates:", result)

