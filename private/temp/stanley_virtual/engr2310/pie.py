# Cameron Stanley
# 2/9/2021
# This code askes you how many terms you want to calculate to get pie and then calculates to get pie.

k = int(input("How many terms do you want"))
num = 1
den = -1
y = 0
sign = -1
i = 0 # keeps the loop going.
while i == 0:
    den+=2 #makes the denomanator go up by two each loop.
    sign = sign * -1 # changes the numberator from positve to negative every other loop.
    y = ((sign * num) /den ) + y
    k = k - 1
    if k == 0: # breaks the loop.
        y = 4 * y # the final calcuation to get pie.
        print(y)
        break
