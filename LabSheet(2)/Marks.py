m=int(input("enter your marks : "))
if m >=90 and m <=100:
    print("grade:A")
elif m >=75 and m <=89:
    print("grade :B")
elif m>=50 and m <=74:
    print("grade :C") 
elif m<50 and m>=0:
    print("grade:F")
else:
    print("invalid marks")          