class Robot:
    def action(self):
        print('Robot in action')


class HelloRobot(Robot):
    def action(self):
        print('Hello world')


class ByeRobot(Robot):
    def action(self):
        print('Started.')


r = HelloRobot()
d = ByeRobot()
x = Robot()
r.action()
d.action()
x.action()
