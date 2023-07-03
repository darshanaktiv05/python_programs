# fifth program
string1 = input("enter a string: ")


def count_char():
    di = {}
    for i in string1:
        keys = di.keys()
        if i in keys:
            di[i] += 1
        else:
            di[i] = 1
    print(di)


count_char()
