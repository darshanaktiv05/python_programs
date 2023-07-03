s_1 = input("Enter first string: ")
s_2 = input("Enter second string: ")

l1 = list(s_1)
l2 = list(s_2)
l2.reverse()

x = zip(l1, l2)
string = ""

for a, b in x:
    string += (a + b)

print(string)
