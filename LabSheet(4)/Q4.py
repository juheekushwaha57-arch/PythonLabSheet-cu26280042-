# 4. Find the product of all elements in a list

numbers = list(map(int, input("Enter numbers: ").split()))

product = 1

for num in numbers:
    product *= num

print("Product:", product)

