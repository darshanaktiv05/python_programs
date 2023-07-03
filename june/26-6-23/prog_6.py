class vehicls():
    def __init__(self):
        self.charge = 100
        self.seats = 50
        self.total = self.seats * self.charge


class bus(vehicls):

    def tot_ch(self):
        super().__init__()
        extra_charge = (self.total * 10) / 100
        total_charge = extra_charge + self.total
        print(total_charge)


obj = bus()
obj.tot_ch()
