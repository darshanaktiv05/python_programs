# eight program
class Bank:
    def __init__(self):
        self.bal = 0
        print("Welcome to the ATM Machine.....................")

    def deposit(self):
        amount = float(input("how many amount you want to deposit: "))
        self.bal += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("how many amount you want to withdraw: "))
        if self.bal >= amount:
            self.bal -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance ")

    def display(self):
        print("\n Net Available Balance=", int(self.bal))


s = Bank()

while True:
    n = int(input("\n press 1 for deposit\n press 2 for withdraw\n press 3 for display \n press 0 for exit: "))
    if n == 1:
        s.deposit()
    elif n == 2:
        s.withdraw()
    elif n == 3:
        s.display()
    else:
        exit()
