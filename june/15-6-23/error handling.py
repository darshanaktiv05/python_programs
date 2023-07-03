lis1 = [1, 2, 3, 4, 5]

lis1 = iter(lis1)

print("Values at 1st iteration : ")
for i in range(0, 5):
    print(next(lis1))

print("Values at 2nd iteration : ")
for j in range(0, 5):
    print(next(lis1))
