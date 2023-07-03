# class Grandparent(object):
#     def my_method(self):
#         print("Grandparent")
#
#
# class Parent(Grandparent):
#     def my_method(self):
#         print("Parent")
#
#
# class Child(Parent):
#     def my_method(self):
#         print("Hello Grandparent")
#         Grandparent.my_method(self)


class student():
    def dd(self, id, fname, lname):
        self.id = id
        self.lname = lname
        self.fname = fname


class Freelance(student):
    def __init__(self, id, fname, lname, Emails):
        super().dd(id, fname, lname)
        self.Emails = Emails


Emp_1 = Freelance(101, "sagar", "patel", "123sagar@gmial.como")
print('The ID is:', Emp_1.id, '\nThe Name is: ', Emp_1.fname, '\nThe Name is:', Emp_1.lname, '\nThe Emails is:', Emp_1.Emails)
