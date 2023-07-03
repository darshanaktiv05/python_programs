def evens():
    for i in range(0, 30, 2):
        # if i % 2 == 0:
        print(i)


evens()

print(list(filter(lambda num: num % 2 == 0, range(1, 30 + 1))))
