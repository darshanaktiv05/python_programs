# Creating a menu view
def showMenu():
    print("Welcome to Contact Books. What do you want to do?")
    print("1. View contact")
    print("2. Change contact")
    print("3. Add contact")
    print("4. Delete contact")
    print("5. Exit")


contacts = {
    1: {
        "name": "Emil",
        "number": 219818,
        "address": "76 Buttonwood Street Valdosta"
    },
    2: {
        "name": "Tobias",
        "number": 2871238,
        "address": "566 Panama City, FL 32404"
    },
    3: {
        "name": "Linus",
        "number": 12323,
        "address": "76 Bellevue St. Beaver Falls"
    }
}


def selectMenu():
    repeat = True
    while True:
        try:
            option = int(input("Choose[1-5]: "))
        except ValueError:
            print("Please input number.")
            # fill the option with 0 so the application won't error
            option = 0
        if option > 0 and option < 6: repeat = False
        if option == 1:
            # showContacts()
            # showMenu()
            print(contacts)
            print("1 selected")
        elif option == 2:
            print("\n==============")
            print("Change Contact")
            print("==============")
            # updateContact()
            # showMenu()
        elif option == 3:
            print("\n===========")
            print("Add Contact")
            print("===========")
            # addContact()
            # showMenu()
        elif option == 4:
            # deleteContact()
            # showMenu()
            print("4 selected")
        elif option == 5:
            print("Good bye!")
            break
        else:
            print("Option unavailable.")


showMenu()
selectMenu()
