dicts = []
while True:
    print("1. enter data")
    print("2. update data")
    print("3. delete data")
    print("4. search data")
    print("5. display data")
    print("6. exit")

    choose = int(input("what you want to choose: "))

    if choose == 1:
        name = input("Enter name: ")
        email = input("Enter email: ")
        phone_number = int(input("Enter phone number: "))

        # for i in dicts:
        #     if email == i.get('email'):
        #         print("email is already exist in the data.")
        #     else:
        #         print()

        temp = {'name': name, 'email': email, 'phone_number': phone_number}
        dicts.append(temp)
    elif choose == 2:
        print("1. email\n2. contact")
        get = int(input("select what you want to update: "))
        if get == 1:
            old_email = input("enter old email: ")
            for i in dicts:
                if old_email == i['email']:
                    new_email = input("enter new email. ")
                    i['email'] = new_email
        elif get == 2:
            old_phone = int(input("enter old phone number: "))
            print(old_phone)
            for i in dicts:
                if old_phone == i['phone_number']:
                    print(old_phone)
                    new_phone = int(input("enter new phone number. "))
                    i['phone_number'] = new_phone

        else:
            print("enter valid number.")

    elif choose == 3:
        name = input("Enter Name of the Contact to Delete: ")
        found = False
        for contact in dicts:
            if contact['name'] == name:
                dicts.remove(contact)
                found = True
                print("Contact deleted successfully.")
                break
        if not found:
            print("Contact not found.")

    elif choose == 4:
        search_email = input("Enter email which you want to search: ")

        for key in dicts:
            if key['email'] == search_email:
                print("Email found", search_email)
            else:
                print("Email not found")

    elif choose == 5:
        print(dicts)

    else:
        print("exit")
        break
