def get_numbers():
    N = int(input("How many numbers you want to enter: "))
    li = []
    if N != 0:
        for i in range(N):
            num = int(input("Enter a number: "))
            li.append(num)
        print(num)

        def sum_of_numbers():
            total = sum(li)
            print("Total of the numbers is: ", total)

            def avg_of_numbers():
                avg = total / N
                print("Average of that numbers is: ", int(avg))

            avg_of_numbers()

        sum_of_numbers()
    else:
        print("Please enter positive number.")


get_numbers()
