# 23. Convert two lists into a dictionary

keys = input("Enter keys separated by spaces: ").split()
values = input("Enter values separated by spaces: ").split()

if len(keys) == len(values):
    result = dict(zip(keys, values))
    print("Dictionary:", result)
else:
    print("Both lists must have the same length")
    
