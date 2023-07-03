li1 = [1, 2, 3, 4, 5]
li2 = [22, 55, 97]

squere = list(map(lambda x, y: x + y, li1, li2))
print(li1)
print(li2)
print(squere)

lst = ['fri', 'sat', 'sun', 'mon']

days = list(map(list, lst))
print(days)

import math

li = [9, 16, 25, 36]
x = list(map(math.sqrt, li))
print(x)
