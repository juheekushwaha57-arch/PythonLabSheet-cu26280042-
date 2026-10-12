# 17. Update the value of a key in a dictionary

student = {"name": "Rahul", "age": 20, "marks": 75}

key = input("Enter key to update: ")
value = input("Enter new value: ")

if key in student:
    student[key] = value
    print("Updated dictionary:", student)
else:
    print("Key does not exist")
    
