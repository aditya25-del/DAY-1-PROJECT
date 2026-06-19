n = 5
for i in range(n, 0, -1):
    print("*" * i)


    n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


    n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(chr(64 + i), end="")
    print()


    n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
         print("*", end="")
        else:
            print(" ", end="")
    print()

    