n = 5
for i in range(1, n + 1):
    print("*" * (2 * i - 1))

n = 5
for i in range(n, 0, -1):
    print("*" * (2 * i - 1))

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

    n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end="")
    print()