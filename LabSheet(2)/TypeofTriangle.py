a=int(input("enter first side ="))
b=int(input("enter second side ="))
c=int(input("enter third side ="))
if a==b and b==c:
    print("equilarteral triangle")
elif a==b or b==c or a==c:
    print("isosceles triangle")
else:
    print("scalene triangle")        
