# Cameron Stanley
# 2-19-2021
# This code has a number. It will ask you to guess a number. If you guess right it will tell you.
# If you are wrong it will keep having you guess.
z = 0
while  z == 0:# makes the loop go
    x = int(input("Guess a number. "))
    if x == 5:
        print("You guessed right")
        break#stops the loop if you are right
    else:
        continue#keeps the loop going to you get the right number.
    
