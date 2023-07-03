l1 = [7, 24, 65, 36, 42, 28]

new_l1 = ["true" if i % 6 == 0 else "false" for i in l1]
print(any(new_l1))
