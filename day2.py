n=int(input("Enter a number:"))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit 
    n=n//10
    print("Sum of digits=",sum)

n=int(input("Enter a number:"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
    print("Reversed number=",rev)

n=int(input("Enter a number:"))
product=1
while n>0:
    digit=n%10
    product=product*digit
    n=n//10
    print("Product=",product)

n=int(input("Enter a number:"))
original=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
    if original==rev:
        print("Palindrome")
    else: print("Not Palindrome")
    