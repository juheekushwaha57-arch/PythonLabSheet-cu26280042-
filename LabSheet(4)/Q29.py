# 29. Find common keys between two dictionaries

dict1 = {"a": 10, "b": 20, "c": 30, "d": 40}
dict2 = {"b": 50, "c": 60, "e": 70}

common_keys = []

for key in dict1:
    if key in dict2:
        common_keys.append(key)

print("Common keys:", common_keys)
