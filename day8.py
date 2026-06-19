n = 5
for i in range(1, n + 1):
    print("*" * i)


n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


    n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()


    n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()

    