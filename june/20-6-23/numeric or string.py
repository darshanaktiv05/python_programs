# find how many characters and numbers are in input

st = input("Enter something: ")
dig = num = 0
for i in st:
    if i.isalpha():
        dig = dig + 1
    elif i.isdigit():
        num = num + 1
    else:
        print("others are special characters.")
print("total characters are: ", dig)
print("total numbers are: ", num)
