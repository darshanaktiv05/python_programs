class car:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def names(self):
        print(self.name)

    def p(self):
        print(self.color)
        print(self.price)


c3 = car("Volvo", 'blue', "1000000")

c3.names()
c3.p()
