n=int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    print("Sum=",sum)

    n=int(input("Enter a number:"))
    for i in range(1,11):
        print(n,"x",i,"=",n*i)

n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print("Factorial=",fact)

n=int(input("Enter a number:"))
count=0
while n>0:
    n=n//10
    count =count+1
    print("Number of digits=",count)
        