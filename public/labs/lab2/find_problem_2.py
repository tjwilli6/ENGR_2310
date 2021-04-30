username_correct = 'Dwight'
pwd_correct = 'beets'
username = input('Enter your username: ')
pwd = input('Enter your password: ')
if username == username_correct:
    authenticate = True
elif pwd == pwd_correct:
    authenticate = True
else:
    authenticate = False
if authenticate:
    print("Welcome, ", username)
else:
    print("Authentication failed")
