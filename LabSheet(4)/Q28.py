# 28. Create a nested dictionary for student details (Name, Roll, Marks)

students = {
    "Student1": {
        "Name": "Rahul",
        "Roll": 101,
        "Marks": 85
    },
    "Student2": {
        "Name": "Priya",
        "Roll": 102,
        "Marks": 92
    },
    "Student3": {
        "Name": "Aman",
        "Roll": 103,
        "Marks": 78
    }
}

for student, details in students.items():
    print(student, ":", details)

