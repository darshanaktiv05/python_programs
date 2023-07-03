def power_of_digit():
    try:
        digit = int(input("enter one digit: "))
        power = int(input("enter power of digit: "))

        powered_number = digit ** power

        print(powered_number)
    except Exception as e:
        print("there is some error: ", e)


power_of_digit()
