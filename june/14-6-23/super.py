# class student():
#     def dd(self, id, fname, lname):
#         self.id = id
#         self.lname = lname
#         self.fname = fname
#
#
# class Freelance(student):
#     def __init__(self, id, fname, lname, Emails):
#         self.id = id
#         self.fname = fname
#         self.lname = lname
#         self.Emails = Emails
#
#
# Emp_1 = Freelance(101, "sagar", "patel", "123sagar@gmial.como")
# print('The ID is:', Emp_1.id, '\nThe Name is: ', Emp_1.fname, '\nThe Name is:', Emp_1.lname, '\nThe Emails is:',
#       Emp_1.Emails)


class Pet():
    def hello(self): print("Hello, I am a Pet")


class Cat(Pet):
    def hello_there(self): print("Hello there! I am a Pet")

    def say(self):
        super().hello()
        self.hello_there()


mycat = Cat()
mycat.say()
