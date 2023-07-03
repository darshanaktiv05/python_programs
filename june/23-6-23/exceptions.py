x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and a str")


finally:
    print("This is the last phase of this code")
