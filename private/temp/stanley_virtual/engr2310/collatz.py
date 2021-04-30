#Cameron Stanley
#2-26-2021
# This code askes for any number and then calculates it by putting it into a Collatz problem.

num = int(input("Enter a number: ")) #Is the input for the number.
x = 0#makes the loop
def collatz(num):#The function for Collatz problem
    if (num % 2) == 0:
        num = num/2
        print(num)
        return num

    else:
        num = (num * 3) + 1
        print(num)
        return num

while x == 0:#the loop that gets the number to 1.
    num = collatz(num)
    if num == 1:
        #print(num)
        break
    else:
        continue

