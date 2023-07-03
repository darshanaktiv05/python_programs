d = {'a': 1, 'e': 2, 'c': 3, 'd': 5, 'j': 8}

for i, j in d.items():
    if i > 'd':
        if j > 2:
            print(i, j)

x = {i: j for i, j in d.items() if i > 'd' and j > 2}
print(x)
