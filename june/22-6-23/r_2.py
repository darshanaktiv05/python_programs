def d_1(func):
    def inner1():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")

    return inner1


def function_to_be_used():
    print("This is inside the function !!")


function_to_be_used = d_1(function_to_be_used)
function_to_be_used()
