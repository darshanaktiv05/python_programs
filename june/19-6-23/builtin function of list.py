L1 = [1, 2, 3, 4, 5]
L2 = [6, 7, 8, 9, 10]
L3 = [100, 200]
L4 = 0
L5 = 0
car1 = ['Volvo', 'Mahindra', 'TATA', 'Mclaren']


# print(cmp(L1))
print(len(car1))
print(max(L1))
print(max(car1))
print(min(L1))
print(min(car1))

L1.append(500)
print(L1)

L4 = L1.copy()
print(L4)

L5 = L2.count(500)
print(L5)

L1.extend(L2)
print(L1)

x = L1.index(4)
print(x)
x = car1.index('Mahindra')
print(x)

print(car1.pop())

car1.reverse()
print(car1)

