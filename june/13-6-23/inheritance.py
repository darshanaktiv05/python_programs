class cars:
    def name(self):
        print("Car name is: Volvo")


class models():
    def accessories(self):
        print("The accessories of car is: Tires")


class brand(models, cars):
    def prices(self):
        print("Car price in $")


obj = brand()
obj.name()
obj.accessories()
obj.prices()


