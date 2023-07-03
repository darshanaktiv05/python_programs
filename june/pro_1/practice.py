# import platform
# if platform.system() == "Linux":
#     print("Linux")
# elif platform.system() == "Windows":
#     print("Windows")
# else:
#     print("Mac")
#


# import pkg_resources
#
# installed_packages = pkg_resources.working_set
# installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
# print(installed_packages_list)

# li = ['new', "list", 1, 836, '264', '%']
# li.append(5)
# li.extend([5, 6, 7])
# li.insert(2, 30)
#
# print("new list is: ", li)
#
# s1 = {1, 2, 3}
# s2 = {4, 5, 6}
# s3 = s1.union(s2)
# print("union of two sets is: ", s3)
#
# st = "first new string"
# print("original string is: ", st)
# print("first two letters of string is: ", st[:2])
# print("length of string is: ", len(st))
#
# l1 = [1,23,5,2,60,9]
# print("sum of all items of the list is: ",sum(l1))
# print(st.count(st))
#
# A = input("enter something: ")
# if A.isnumeric():
#     print("it is a number.")
# else:
#     print("it is string.")

# def Merge(d1, d2):
#     return d2.update(d1)


# d1 = {'a': 10, 'b': 20}
# d2 = {'x': 100, 'z': 1000}
# d1.update(d2)
# print(d1)

# d1 = {'a': 421, 'b': 716, 'x': 50, 'z': 1001, 'p': 621}
# x1 = sorted(d1.items(), key=lambda x: x[1])
# print(x1)

# l1.sort()
# print(max(l1))


# import numpy as np
#
# R = int(input("Enter the number of rows:"))
# C = int(input("Enter the number of columns:"))
#
# print("Enter the entries in a single line (separated by space): ")
#
# entries = list(map(int, input().split()))
#
#
# matrix = np.array(entries).reshape(R, C)
# print(matrix)

# this accepts the user's input
# and stores in inp

# A = int(input("enter a number: "))
# for n in range(1, A+1):
#     prime = True
#     for x in range(2, n):
#         if n % x == 0:
#             prime = False
#             print(n, " is not prime")
#
#     if prime:
#         print(n, " is prime!")
