password = "star wars"

while password == "star wars":
    password = input("password required: ")
    if password != "star wars":
        print("Access failed")
    elif password == "star wars":
        print("Access granted")
        print("Welcome, Mastor Jedi")
        y = input("What is your name: ")
        x = input("Do you want to know a secret: ")
        if x == "yes":
            print("You are not the last Jedi!", y)
            print("Have a nice day Mastor Jedi!")
            break
        else:
            print("OK")
            print("Have a nice day Mastor Jedi")
            break
