# print even numbers from list using lambda function with filter

numbers = [22, 35, 98, 32, 41, 7]

x = list(filter(lambda x: x % 2 == 0, numbers))
print(x)
