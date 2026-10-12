# 1. Find the sum and average of elements in a list

numbers = list(map(int, input("Enter numbers: ").split()))

total = sum(numbers)

if len(numbers) > 0:
    average = total / len(numbers)
    print("Sum:", total)
    print("Average:", average)
else:
    print("List is empty")
    
