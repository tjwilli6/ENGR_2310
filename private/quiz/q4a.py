user_input = 1
while user_input % 2:
    user_input = int(input("Enter a number"))
    if user_input % 2 == 1:
        continue
    print("You entered an even number!")

