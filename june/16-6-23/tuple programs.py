tup1 = (1,2,3)
tup2 = (4,5)
tup = tup1 + tup2
print(tup)
# tup = (1,2,3,4,5)
li = list(tup)
li[2] = 'hello'
tup = tuple(li)
print(tup)
