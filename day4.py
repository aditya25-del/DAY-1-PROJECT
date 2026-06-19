n = int(input("Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c


    n = int(input("Enter n: "))
a = 0
b = 1
for i in range(n - 1):
    c = a + b
    a = b
    b = c
print("Nth Fibonacci term =", a)

n = int(input("Enter a number: "))
temp = n
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit ** 3
    n = n // 10
if temp == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")


    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
for n in range(start, end + 1):
    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** 3
        temp = temp // 10
    if n == sum:
        print(n)

        