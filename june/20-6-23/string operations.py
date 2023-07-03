# string methods and builtin functions

s1 = input("Enter one string: ")
print(" 1. Make capitalize\n 2. Want center\n 3. Make upper\n 4. Make title\n 5. Swap case\n "
      "6. Is alpha numeric\n 7. Make split\n 8. All string except last wo characters\n "
      "9. Just last two characters\n 10. Start from fifth character.")
while True:
    n1 = int(input("Enter one number: "))

    if n1 == 1:
        ss = s1.capitalize()
        print("Capitalization of entered string: ", ss)

    elif n1 == 2:
        ss = s1.center(50)
        print("Center of entered string: ", ss)
    elif n1 == 3:
        ss = s1.upper()
        print("Convert in to upper case of entered string: ", ss)
    elif n1 == 4:
        ss = s1.title()
        print("Convert into title form: ", ss)
    elif n1 == 5:
        ss = s1.swapcase()
        print("Swap case of entered string: ", ss)
    elif n1 == 6:
        ss = s1.isalnum()
        print("Entered string is alpha numeric or not: ", ss)
    elif n1 == 7:
        ss = s1.split()
        print("Split the entered string: ", ss)
    elif n1 == 8:
        ss = s1[:2]
        print("Only first two character of entered string: ", ss)
    elif n1 == 9:
        ss = s1[:-2]
        print("Only last two character of entered string: ", ss)
    elif n1 == 10:
        ss = s1[5:]
        print("String start from fifth character of entered string: ", ss)
    else:
        print("Enter number between 1 to 10.")
        break
