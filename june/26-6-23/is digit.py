# num = int(input("Enter the number"))
# digit = int(input("Enter a Digit"))
# count = 0
# n = num
# while n != 0:
#     rem = n % 10
#     if rem == digit:
#         print("{} is occured in {}".format(digit, num))
#         break
#     n = n // 10
# else:
#     print("{} is not occured in {}".format(digit, num))

# COUNT VOWELS AND CONSONANTS
# string = input("Enter a String: ")
# vowels = 0  # variable to count number of vowels
# consonants = 0  # variable to count number of consonants
# for i in string:  # string iteration
#     if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):  # if character in string is vowel
#         vowels += 1  # if vowel increment variable ‘vowel’ with one
#     elif i.isalpha():  # checking if the character is alphabet
#         consonants += 1  # if consonant increment variable ‘consonants’ with one
# print("Vowels:", vowels, "Consonants:", consonants)


# PRINT fahrenheit INTO CELSIUS
# fahrenheit = float(input("Please give the Fahrenheit Temperature : "))
# # converting Celsius into Fahrenheit
# celsius = (fahrenheit - 32) * 5 / 9
# print("Celsius = ", celsius)


# FIND FECTORIAL USING RECURSION

# def fact(n):
#     if n == 1:
#         return n
#     else:
#         # recursion
#         return n * fact(n - 1)
#
#
# num = int(input("Enter a whole number to find Factorial: "))
# if num < 0:
#     print("Factorial can’t be calculated for negative number")
# elif num == 0:
#     print("Factorial of 0 is 1")
# else:
#     print("Factorial of", num, "is", fact(num))

# LCM

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#     greater = num1
# else:
#     greater = num2
# while True:
#     if (greater % num1 == 0) and (greater % num2 == 0):
#         lcm = greater
#         break
#     greater += 1
# print("LCM of", num1, "and", num2, "=", greater)
