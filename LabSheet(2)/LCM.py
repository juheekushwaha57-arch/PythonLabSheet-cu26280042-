a=int(input("enter first no. ="))
b=int(input("enter second no. ="))
lcm=max(a,b)
while lcm%a!=0 or lcm%b!=0:
    lcm=lcm+1
print("lcm =",lcm)

