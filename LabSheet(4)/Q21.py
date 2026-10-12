# 21. Find the key with the maximum value in a dictionary

data = {"Rahul": 85, "Priya": 92, "Aman": 78, "Neha": 88}

if data:
    max_key = max(data, key=data.get)
    print("Key with maximum value:", max_key)
    print("Maximum value:", data[max_key])
else:
    print("Dictionary is empty")
    
