list1 = ['1000', '9999', '1504']
result = []
for i in range(999,1000):
    if len(i) == 4:
        number1 = str(i)
        secound_number = int(number1[1])
        last_number = int(number1[-1])
        if secound_number % 2 != 0 and last_number % 2 == 0 and (int(i) % 8 == 0 or int(i) % 5 == 0):
            result.append(i)
m = map(result)
print(m)