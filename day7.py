def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
n = int(input("Enter a number: "))
print("Factorial =", factorial(n))


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter n: "))
print("Nth Fibonacci term =", fibonacci(n))


def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)
n = int(input("Enter a number: "))
print("Sum of digits =", sum_digits(n))


def reverse(n, rev=0):
    if n == 0:
        return rev
    digit = n % 10
    rev = rev * 10 + digit
    return reverse(n // 10, rev)
n = int(input("Enter a number: "))
print("Reversed number =", reverse(n))