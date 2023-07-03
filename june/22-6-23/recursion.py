def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x != 1:
        return x * factorial(x - 1)
    else:
        return 1


num = int(input())
print("The factorial of", num, "is", factorial(num))
