#Cameron Stanley
#2-7-2021
# This program will convert binary to decimal.
# the way it works is you enter one digit at a time in binary from
# then you enter a number that is not 1 or 0 and it tells you the decimal form
# the binary number that you entered.
n = -1
# n is negative one because in the loop n is getting +1 in each loop and you need to start with 0
# -1 + 1= 0 then keep adding 1 each loop.
c = 0
# c is zero so the loop will keep going till you stop it.
y = 0
# y is zero so the loop will remember what y was from the previous loop. 
while c == 0:
    x = int(input("Enter number"))
    n+=1
    if x == 1 or x ==0: #if the number you input is not 0 or 1 then it won't put that number in the equation and will end the loop. 
        y = x*(2**n) + y # the equation is what ever x is times 2 to n power + the previous loops equation.
        continue
    else:#only prints final result
        print(y)
        break
        
