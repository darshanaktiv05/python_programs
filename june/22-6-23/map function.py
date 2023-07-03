# # Add two lists using map and lambda
#
# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
#
# result = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result))


# l = ['sat', 'bat', 'cat', 'mat']
#
# # map() can listify the list of strings individually
# test = list(map(list, l))
# print(test)


# def mul(i):
#     return i * i
#
#
# x = list(map(mul, (3, 5, 7, 11, 13)))
#
# print(x)


def mul(i):
    return i * i


num = (3, 5, 7, 11, 13)

resu = map(mul, num)

print(resu)

# making the map object readable

mul_output = list(resu)

print(mul_output)
