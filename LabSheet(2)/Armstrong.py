num=int(input("enter a number : "))
ori=num
arms=0
r=0
while( num>0):
    r=num%10
    arms=arms+r*r*r
    num = num//10
if ori==arms:
    print("the number is a armstrong")
else:
    print("the number is not a armstrong")
