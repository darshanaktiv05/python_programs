a = ""
i = 0
for j in range(4):
    a = a + " "
print(a + "*")
a = ""
j = 0
for i in range(3):
    for j in range(3 - i):
        a = a + " "
    a = a + "*"
    for k in range(2 * i + 1):
        a = a + " "
    a = a + "*"
    print(a)
    j = 0
    k = 0
    a = ""
for i in range(4):
    for j in range(i):
        a = a + " "
    a = a + "*"
    for k in range(7 - 2 * i):
        a = a + " "
    a = a + "*"
    print(a)
    j = 0
    k = 0
    a = ""
for j in range(4):
    a = a + " "
print(a + "*")
