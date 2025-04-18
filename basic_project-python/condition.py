#make a name , email, or password formate in python--
name = input("enter your name: ")
email = input("enter E-mail: ")
password = input("create password: ")

if name == " ":
    print("please enter your name;")
else:
    if "@" not in email:
        print("please enter a valid E-mail;")
    else:
        if len(password) <=8:
            print("make a strong password (<= 8).")
        else:
            print("login succesfully")