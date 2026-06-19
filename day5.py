n = int(input("Enter a number: "))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum = sum + i
if sum == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")


    n = int(input("Enter a number: "))
temp = n
sum = 0
while n > 0:
    digit = n % 10
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i
    sum = sum + fact
    n = n // 10
if temp == sum:
    print("Strong Number")
else:
    print("Not Strong Number")


    n = int(input("Enter a number: "))
print("Factors are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)


        n = int(input("Enter a number: "))
        largest = 1
for i in range(2, n + 1):
    if n % i == 0:
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count = count + 1
                if count == 2:
                 largest = i
print("Largest Prime Factor =", largest)


