def get_numbers():

    n1 = int(input("enter first number: "))
    n2 = int(input("enter second number: "))
    n3 = int(input("enter third number: "))
    avg = 0

    def sum_of_numbers():
        nonlocal avg
        avg = n1 + n2 + n3
        print("the total of numbers is: ", avg)

        def avg_of_numbers():
            nonlocal avg
            avg = avg / 3
            print("the average of numbers is: ", avg)

        avg_of_numbers()

    sum_of_numbers()


get_numbers()
