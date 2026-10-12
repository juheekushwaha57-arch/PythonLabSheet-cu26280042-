# 29. Find the difference between two lists

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

difference = []

for num in list1:
    if num not in list2 and num not in difference:
        difference.append(num)

print("Elements in first list but not in second:", difference)

