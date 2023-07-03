# convert temperatures from Celsius to Fahrenheit using lambda function with map()

numbers = [22, 30, 15, 28]

x = list(map(lambda x: (x * 1.8) + 32, numbers))
print(x)
