# # if, in, and, elif, or, is, not, else, not
#
# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
#
# if 1 in b and 8 in b:
#     print("This Is Ture.....")
# elif 7 in a and 3 not in b:
#     print("This Is All False.....")
# elif a is b:
#     print("Both Are Same.....")
# else:
#     print("Check Your The List.....")
#
# # from, import, as
#
# from datetime import datetime as dt
#
# now = dt.now()
#
# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)
#
# # for, in, range, while, break
#
# for i in range(0, 5):
#     j = 0
#     while j <= i:
#         print(":*:", end=" ")
#         j += 1
#         # break
#     print()
#
#
# # class, try, except, finally, pass, def, raise
#
# class Keywords:
#     def pass_statement(self):
#         pass
#
#     def divide(x, y):
#         try:
#             res = x / y
#             print("Yeah ! Your answer is :", res)
#
#         except ZeroDivisionError:
#             print("Sorry ! You are dividing by zero ")
#         finally:
#             print("This program written in PyCharm")
#         raise Exception("This is not proper format for this code.")
#
#     divide(3, 0)
#
#
# # lambda, in, for
#
# its_even = [lambda arg=x: arg * 25 for x in range(1, 5)]
#
# for i in its_even:
#     print(i())
#
#
# def fun1():
#     yield "Welcome To"
#     yield "Simplifiable"
#
#
# gen_object = fun1()
# print(gen_object)
# print(type(gen_object))
#
# for i in gen_object:
#     print(i)
#
# for i in range(1, 10):
#     if i == 5:
#         continue
#     elif i == 7:
#         break
#     else:
#         print(i)
#
#
# def filter_even(numbers):
#     for number in range(numbers):
#         print(number)
#         if number % 2 == 0:
#             return number
#
#
# odd_numbers = filter_even(10)
# print(odd_numbers)
# for num in odd_numbers:
#     print(num)


# with open('new.py', 'w') as file:
#     file.write("this is new file made by code in python.")
#
# import os
#
# if os.path.exists("new.py"):
#     os.remove("new.py")
# else:
#     print("The file does not exist")


# with open("new.py") as input_file:
#     for name in input_file:
#         print(name.strip())


# def newf():
#     global A
#     A = 10
#     # print(A)
# newf()
# print(A)
#
# def newf1():
#      yield "this is new function"
#      yield "for the yield and globle"
#
# N = newf1()
#
# print(next(N))
# print(next(N))