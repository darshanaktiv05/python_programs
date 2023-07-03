# def myfunc1():
#     x = "John"
#
#     def myfunc2():
#         x = "hello"
#
#     myfunc2()
#     return x
#
#
# print(myfunc1())


def outside():
    x = "local"

    def inside():
        nonlocal x
        x = "nonlocal"
        print("inside: ", x)

    inside()
    print("outside: ", x)


outside()