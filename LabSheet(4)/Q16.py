# 16. Sort a dictionary by values

data = {"Rahul": 85, "Priya": 92, "Aman": 78, "Neha": 88}

sorted_dict = dict(sorted(data.items(), key=lambda item: item[1]))

print("Dictionary sorted by values:", sorted_dict)

