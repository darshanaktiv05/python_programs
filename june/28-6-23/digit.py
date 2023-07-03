list1 = [1000, 1540, 15566, 2461, 2134]
list2 = []
for i in list1:
    if i >= 1000 and i <= 9999:
        all1 = i % 10
        all_second = i // 100
        all_check = all_second % 10
        if all1 % 2 == 0 and all_check % 2 > 0:
            print(all1, all_check)
            if i % 8 == 0 and i % 5 == 0:
                print(i)
                list2.append(i)
print(list2)
