username_correct = 'Dwight'
pwd_correct = 'beets'
username = input("Enter your username: ")
pwd = input("Enter your password: ")
if username == username_correct and pwd == pwd_correct:
    print("Welcome, ", username)
else:
    print("Authentication failed")
