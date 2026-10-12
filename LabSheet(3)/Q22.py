
# 22. Sort a list in ascending and descending order

numbers = list(map(int, input("Enter numbers: ").split()))

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Ascending order:", ascending)
print("Descending order:", descending)

