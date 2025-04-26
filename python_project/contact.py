#empty dictionary
contacts={}
while True:
    print("\n contact formate App")
    print("1. create contact")
    print("2. view contact")
    print("3. update contact")
    print("4. delete contact")
    print("5. search contact")
    print("6. count contact")
    print("7. exit from contact")

    choice = input('enter your choice: ')

    if choice == '1':
        name = input("enter your name: ")
        if name in contacts:
            print(f"contact name {name} already exist")
        else:
            number = input("enter your number: ")
            add = input("enter your address: ")
            email = input("enter your email-id: ")
            contacts[name] = {'email':email, 'number': int(number), 'add': add}
            print(f"contact name {name} has been saved.")

    elif choice == '2':
        name = input("enter contact name to view: ")
        if name in contacts:
            contacts = contacts[name]
            print(f"contact: \n {name} : {number} and e-mail:{email},address:{add}.")
        else:
            print(f"{name} not found in contact!")

    elif choice == '3':
        name = input("enter contact name to update: ")
        if name in contacts:
            number = input("enter updated number: ")
            add = input("enter updated address: ")
            email = input("enter updated email-id: ")
        else:
            print(f'{name} not found!')
    
    elif choice == '4':
        name = input("enter name to delete:")
        if name in contacts:
            del contacts[name]
            print(f"contact name {name} has been deleted!")
        else:
            print(f'{name} not found!')

    elif choice == '5':
        s_name = input("enter name to search: ")
        found = False
        for s_name , number in contacts.items():
            if s_name.lower() in name.lower():
                print(f'found -\n name {name}, add {add}, number: {number}, e-mail: {email}')
                found = True
            if not found:
                print(f"{s_name} not found!")

    elif choice == '6':
        print(f'total contacts in my book:{len(contacts)}')

    elif choice == '7':
        print("closing contacts book app...")
        break

    else:
        print("error!")