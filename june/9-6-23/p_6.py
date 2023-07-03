a = ""
i = 0
for i in range(5):
    for j in range(i):
        a = a + " "
    for k in range(5):
        a = a + "* "
    print(a)
    j = 0
    k = 0
    a = ""

a = ""
i = 0
for i in range(5):
    for j in range(5 - i):
        a = a + " "
    for k in range(5):
        a = a + "* "
    print(a)
    j = 0
    k = 0
    a = ""
