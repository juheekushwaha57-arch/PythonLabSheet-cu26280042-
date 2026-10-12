# 2. Rotate a list by n positions

numbers = list(map(int, input("Enter numbers: ").split()))
n = int(input("Enter rotation positions: "))

if len(numbers) > 0:
    n = n % len(numbers)
    rotated = numbers[-n:] + numbers[:-n] if n != 0 else numbers
    print("Rotated list:", rotated)
else:
    print("List is empty")
