# fifth program
st = input("enter a string: ")


def count():
    d = {}
    for i in st:
        keys = d.keys()
        if i in keys:
            d[i] += 1
        else:
            d[i] = 1
    print(d)


count()
