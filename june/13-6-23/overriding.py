class first:
    def new(self):
        print("this is first class and function.")

    def old(self):
        print("this is second function.")


class second(first):
    def new(self):
        print("this is second class and function.")

    def old(self):
        print("this is second class.")

obj = second()
obj.old()

