st = int(input("enter how many string you want to enter: "))
li = []

for i in range(st):
    ex_st = input("enter a string: ")
    li.append(ex_st)
print("the string of list you have entered: ", li)

for j in li:
    if j[0].islower() and j.isalpha() and j[0] not in 'aeiou':
        print(j)
    else:
        print("please enter first character of string in lower case and it must be consonant.")
