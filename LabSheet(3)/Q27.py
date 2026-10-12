
# 27. Find the second largest number in a list

numbers = list(map(int, input("Enter numbers: ").split()))

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second largest number:", unique_numbers[-2])
else:
    print("Second largest number does not exist")
