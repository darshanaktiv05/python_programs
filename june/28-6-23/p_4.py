num = int(input("how many number you want to enter: "))
num_li = []

for i in range(num):
    number = int(input("enter a number: "))
    num_li.append(number)
print(num_li)

for j in num_li:
    if j > 999 and j < 10000 :
        second = (j // 100) % 10
        if j % 5 == 0 or j % 8 == 0:
            print(j, " number is divisible with 8 or 5")
    else:
        print("please enter number between 1000 to 9999.")
