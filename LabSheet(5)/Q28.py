# write a program to find repeated items in a tuple. 
t = (1, 2, 3, 2, 4, 3, 5, 2)
repeated = tuple(x for x in dict.fromkeys(t) if t.count(x) > 1)
print("Repeated items:", repeated)
