# def myfunc():
#     x = 300
#
#     def myinnerfunc():
#         print(x)
#
#     myinnerfunc()
#
#
# myfunc()


x = 20


def local():

    x = 100
    print("local: ", x)


local()
print("global: ", x)
