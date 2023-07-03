l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 0]
tup = (1, 2, 3, 4, 5)
# len and count function
# print(l1, l2)
# print(len(l1))
# print(len(l2))
#
# print(l1.count(6))
# print(l2.count(6))

# zip function
# z = zip(l1, l2)
# print(list(z))
# print(tuple(z))
# print(set(z))
# print(dict(z))

# tuple len and count
# print(tup)
# print(tup.count(3))
# print(len(tup))

# dict len and count
# d = {1: 'hello', 2: 'world', 3: 'good', 4: 'morning', 5: 'all'}
# print(d)
# print(len(d))

# set len and count
# s = {22, 54, 87, 3, 45, 57}
# print(s)
# print(len(s))
import re
result = re.search(r'Tutorials', 'TP Tutorials Point TP')
print (result.group(0))