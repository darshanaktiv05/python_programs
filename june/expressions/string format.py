# print("The mangy, scrawny stray dog %s gobbled down" % 'hurriedly' + "the grain-free, organic dog food.")
#
# x = 'looked'
# print("Misha %s and %s around" % ('walked', x))
#
# print('Joe stood up and %s to the crowd.' % 'spoke')
#
# print('There are %d dogs.' % 4)
#
# print('The value of pi is: %.4f' % 3.141592)

# v = 12.78
#
# string = "Variable as integer = %d n" \
#          " Variable as float = %.5f" % (v, v)
#
# print(string)
# V = "New sting"
#
# print(f"{V} will give you new line of code")
def inf_sequence():
    num = 0
    while True:
        yield num
        num += 1


for i in inf_sequence():
    print(i, end=" ")
