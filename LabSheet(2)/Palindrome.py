num=int(input("enter a number : "))
ori=num
rev=0
while num>0:
    digit = num%10
    rev = rev*10+digit
    num = num//10
if ori==rev:
    print("the number is a palindrome ")
else:
    print("the number is not a palindrome")        
