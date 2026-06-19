n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1): 
   if n % i == 0:
        count = count + 1
   if count == 2:
    print("Prime Number")
else:
    print("Not Prime Number")

    
    
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    for n in range(start, end + 1):
     count = 0

    for i in range(1, n + 1):
     if n % i == 0:
         count = count + 1
     if count == 2:
        print(n)

n = int(input("Enter first number: "))
m = int(input("Enter second number: "))

gcd = 1
for i in range(1, min(n, m) + 1):
    if n % i == 0 and m % i == 0:
        gcd = i
print("GCD =", gcd)

n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
largest = max(n, m)
while True:
    if largest % n == 0 and largest % m == 0:
        lcm = largest
        break
    largest = largest + 1
print("LCM =", lcm)