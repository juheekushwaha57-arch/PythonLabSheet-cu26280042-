# 16. Write a program to check if a set is a superset of another set.
s1 = {1, 2, 3, 4}
s2 = {1, 2}

if s1.issuperset(s2):
    print("s1 is a superset of s2")
else:
    print("s1 is not a superset of s2")
