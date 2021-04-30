#Cameron Stanley
#2/19/2021
# This code will have you input a number and then output a number.
#the goal was for the user to find a pattern. This will go on for ever unless you inter 999.

z = 0
def numbers(sum1, sum2):#this is the function
        print("Output = ", ((x*sum1)**sum2))# it is taking the number you input times that number by 4 and then squares it.
while z == 0:# this is the loop
    x = int(input("Input a number. "))
    if x == 999:#ends loop
        break
    numbers(4,2)# calls function
