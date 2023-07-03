n = 5
a = n - 1

for i in range(0, n):
    for j in range(0, a):
        print(end=" ")
    a = a - 1

    for j in range(0, i + 1):
        print("* ", end="")
    print("")

for i in range(n):
    for j in range(0, a, -1):
        print(end=" ")
    a = a - 1

    for j in range(n-1, i, -1):
        print("* ", end="")
    print("")
