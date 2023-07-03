# class Vehicle:
#     def infoo(self):
#         print("This is Vehicle")
#
#
# class Car(Vehicle):
#     def car_infoo(self, name):
#         print("Car name is:", name)
#
#
# class Truck(Car):
#     def truck_infoo(self, name):
#         print("Truck name is:", name)
#
#
# obj1 = Car()
# obj1.infoo()
# obj1.car_infoo('BMW')
#
# obj2 = Truck()
# obj2.infoo()
# obj2.truck_infoo('Tata')


class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")


class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")


class Truck(Vehicle):

    def truck_info(self):
        print("Inside Truck class")


class NewCar(Vehicle):
    def new_car_info(self):
        print("Inside New Car class")


class SportsCar(Car, Truck, NewCar, Vehicle):
    def sports_car_info(self):
        print("Inside SportsCar class")


bus = SportsCar()
bus.car_info()
bus.vehicle_info()
bus.truck_info()
bus.new_car_info()
bus.sports_car_info()
