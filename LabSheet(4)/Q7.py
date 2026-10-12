# 7. Check if a list is sorted or not

numbers = list(map(int, input("Enter numbers: ").split()))

if numbers == sorted(numbers):
    print("List is sorted in ascending order")
else:
    print("List is not sorted in ascending order") 
    
