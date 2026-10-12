# 8. Find pairs whose sum equals a given number

numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))

if pairs:
    print("Pairs:", pairs)
else:
    print("No pairs found") 
    
