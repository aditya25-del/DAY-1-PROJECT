n = int(input("Enter a decimal number: "))
binary = ""
while n > 0:
    rem = n % 2
    binary = str(rem) + binary
    n = n // 2
print("Binary =", binary)


binary = int(input("Enter a binary number: "))
decimal = 0
power = 0
while binary > 0:
    digit = binary % 10
    decimal = decimal + digit * (2 ** power)
    power = power + 1
    binary = binary // 10
print("Decimal =", decimal)


n = int(input("Enter a number: "))
count = 0
while n > 0:
    rem = n % 2
    if rem == 1:
        count = count + 1
    n = n // 2
print("Set bits =", count)


x = int(input("Enter x: "))
n = int(input("Enter n: "))
result = 1
for i in range(n):
    result = result * x
print("Answer =", result)