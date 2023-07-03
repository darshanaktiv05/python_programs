import string
import random  # define the random module

S = 5  # number of characters in the string.
# call random.choices() string module to find the string in Uppercase + numeric data.
ran = ''.join(random.choices(string.ascii_uppercase, k=S))
print("The randomly generated string is : " + str(ran))  # print the random data

print()
print(type(ran))
